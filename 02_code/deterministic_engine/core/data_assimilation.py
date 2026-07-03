import pandas as pd
from core.tree_node import ProcessTreeNode

# PM4Py try-import at module level to prevent blocking unrelated parts of the system.
try:
    import pm4py
    from pm4py.objects.process_tree.obj import Operator
    _PM4PY_AVAILABLE = True
except ImportError:
    _PM4PY_AVAILABLE = False

class DataAssimilation:
    """
    Bridge between external event logs (CSV, XES) and internal application logic. 
    Uses PM4Py to discover process models and converts them to strict binary ProcessTreeNode formats.
    """

    @staticmethod
    def assimilate_from_file(file_path: str, analyzer, noise_threshold: float = 0.0, compute_metrics: bool = True) -> ProcessTreeNode:
        """
        Mine a process tree from a log file and annotate it with frequencies.

        Loads and cleans the log, discovers a process tree via PM4Py's Inductive
        Miner, optionally evaluates conformance metrics, converts the result into
        a strict binary :class:`ProcessTreeNode`, and reconciles its frequencies
        against the true case count using ``analyzer``.

        Args:
            file_path: Path to the event log (CSV or XES-family format).
            analyzer: A :class:`ProcessTreeAnalyzer` used to push the mined
                frequencies onto the converted tree (via ``compute_frequencies``).
            noise_threshold: Inductive-miner noise threshold in ``[0.0, 1.0]``
                controlling how aggressively infrequent behavior is filtered.
            compute_metrics: If ``False``, skips PM4Py's Fitness/Precision
                token-based replay (Step 4 below) -- by far the slowest part of
                this pipeline (observed ~240s/file at noise 0.0 vs. ~4s/file
                without it). Neither the Deterministic Engine's extraction, the
                Trace Verifier's pattern matching, nor the Tree/Data/fractional
                exposure metrics use pm4py_fitness/pm4py_precision at all, so this
                is safe to skip whenever those two headline numbers aren't needed
                for the report (e.g. bulk recalculation of exposure metrics against
                already-audited datasets, where Fitness/Precision can be reused
                from the existing report instead of redone).

        Returns:
            The root :class:`ProcessTreeNode` of the reconciled binary tree, with
            ``pm4py_fitness``, ``pm4py_precision``, and ``binarization_additions``
            attributes attached.

        Raises:
            ImportError: If PM4Py is not installed.
        """
        if not _PM4PY_AVAILABLE:
            raise ImportError(
                "pm4py is required for DataAssimilation but is not installed.\n"
                "Install it with: pip install pm4py"
            )

        # 1. Load and build a pristine, heavily isolated DataFrame
        df_clean = DataAssimilation._prepare_log_dataframe(file_path)

        # 2. Force PM4Py to use EXACTLY our pristine columns.
        df_clean['concept:name'] = df_clean['concept:name'].astype('category')
        log = pm4py.format_dataframe(
            df_clean,
            case_id='case:concept:name',
            activity_key='concept:name',
            timestamp_key='time:timestamp'
        )

        # 3. Mine the tree using Inductive Miner
        pm4py_tree = pm4py.discover_process_tree_inductive(log, noise_threshold=noise_threshold)
        
        # 4. GET METRICS FIRST (Store in temporary variables safely)
        if compute_metrics:
            try:
                net, im, fm = pm4py.convert_to_petri_net(pm4py_tree)
                precision_val = pm4py.precision_token_based_replay(log, net, im, fm)
                fitness_val = pm4py.fitness_token_based_replay(log, net, im, fm)
            except Exception as e:
                fitness_val, precision_val = "N/A", "N/A"
                print(f"\n[Warning] Could not evaluate model metrics: {e}\n")
        else:
            fitness_val, precision_val = "N/A (skipped)", "N/A (skipped)"
        
        # 5. Extract basic node frequencies
        activities = pm4py.get_event_attribute_values(log, "concept:name")
        
        # 6. CREATE ROOT NODE & TRACK BINARIZATION
        binarization_counter = [0]
        root_node = DataAssimilation._convert_node(pm4py_tree, activities, binarization_counter)
        
        # 7. ATTACH METRICS TO ROOT NODE
        root_node.pm4py_fitness = fitness_val
        root_node.pm4py_precision = precision_val
        root_node.binarization_additions = binarization_counter[0]
        
        # 8. Calculate the Absolute Global Truth from the raw log
        global_n = df_clean['case:concept:name'].nunique()
            
        # 9. Push the frequencies mathematically using the Global Anchor!
        analyzer.compute_frequencies(root_node, global_n=global_n)
        
        return root_node

    @staticmethod
    def _prepare_log_dataframe(file_path: str) -> pd.DataFrame:
        """
        Load a log file into a normalized case/activity/timestamp DataFrame.

        Reads the log (CSV or XES-family), then uses semantic data checking --
        inspecting values rather than trusting column names -- to locate the case,
        timestamp, and activity columns, tolerating corrupted or non-standard
        headers. Missing timestamps are replaced with synthetic per-case
        chronological ones.

        Args:
            file_path: Path to the event log to load.

        Returns:
            A DataFrame with exactly the columns ``'case:concept:name'``,
            ``'concept:name'``, and ``'time:timestamp'``.

        Raises:
            ValueError: If the file extension is not supported.
        """
        if file_path.lower().endswith('.csv'):
            try:
                df = pd.read_csv(file_path, sep=None, engine='python', low_memory=False)
            except Exception:
                df = pd.read_csv(file_path, sep=',', low_memory=False)
            if 'Unnamed: 0' in df.columns and df['Unnamed: 0'].is_monotonic_increasing:
                df.drop(columns=['Unnamed: 0'], inplace=True)
        elif file_path.lower().endswith(('.xes', '.xml', '.mxml', '.gz')):
            try:
                log = pm4py.read_xes(file_path)
                df = pm4py.convert_to_dataframe(log)
            except Exception:
                # Fallback to legacy parser if fast parser crashes (e.g. PDC logs)
                from pm4py.objects.log.importer.xes import importer as xes_importer
                log = xes_importer.apply(file_path)
                df = pm4py.convert_to_dataframe(log)
        else:
            raise ValueError(f"Unsupported file extension: {file_path}")

        # 1. Identify Case Column FIRST
        case_col = None
        for cand in ['case:concept:name', 'case id', 'case_id', 'case', 'id']:
            if cand in df.columns:
                case_col = cand
                break
        if not case_col:
            case_col = next((c for c in df.columns if 'case' in c.lower()), df.columns[0])

        # 2. SEMANTIC Time Column Identification (Ignores names, looks at raw data)
        time_col = None
        for c in df.columns:
            if c == case_col: continue
            
            # If it's already a datetime object
            if pd.api.types.is_datetime64_any_dtype(df[c]):
                time_col = c
                break
            
            sample = df[c].dropna().astype(str).head(10)
            if not sample.empty and sample.str.contains(r'^\d{4}-\d{2}-\d{2}|^\d{1,2}/\d{1,2}/\d{2,4}', regex=True).all():
                time_col = c
                break

        # Fallback to names only if semantic check finds nothing
        if not time_col:
            for cand in ['time:timestamp', 'timestamp', 'time', 'date', 'complete timestamp']:
                if cand in df.columns and cand != case_col:
                    time_col = cand
                    break

        # 3. SEMANTIC Activity Column Identification (Excludes time and case)
        valid_cols = [c for c in df.columns if c not in (case_col, time_col)]
        act_col = None
        for cand in ['concept:name', 'activity', 'task', 'event', 'action', 'name']:
            if cand in valid_cols:
                act_col = cand
                break
        if not act_col and valid_cols:
            # Mathematical Fallback: The column with the lowest cardinality is almost always the activity
            act_col = min(valid_cols, key=lambda c: df[c].nunique())

        # 4. Handle Missing Timestamps safely
        if time_col is None or df[time_col].isnull().all():
            print("    [!] Missing timestamps detected. Injecting chronological artificial timestamps...")
            time_col = 'time:timestamp_artificial'
            base_time = pd.Timestamp("2026-01-01 00:00:00")
            df[time_col] = base_time + pd.to_timedelta(df.groupby(case_col, sort=False).cumcount(), unit='s')
        else:
            df[time_col] = pd.to_datetime(df[time_col], errors='coerce')

        # 5. Build the Pristine DataFrame
        df_clean = pd.DataFrame({
            'case:concept:name': df[case_col].astype(str),
            'concept:name': df[act_col].astype(str),
            'time:timestamp': df[time_col]
        })

        return df_clean

    @staticmethod
    def _convert_node(pm_node, activity_counts: dict, binarization_counter: list) -> ProcessTreeNode:
        """
        Recursively convert a PM4Py process-tree node into a ProcessTreeNode.

        Maps PM4Py operators to the internal operator names, turns operator-less
        nodes into (possibly tau) leaves annotated with their activity count, and
        binarizes children with more than two branches.

        Args:
            pm_node: The PM4Py process-tree node to convert.
            activity_counts: Mapping of activity name to its occurrence count.
            binarization_counter: Single-element list used as a mutable counter,
                incremented once per extra binarization node introduced.

        Returns:
            The converted :class:`ProcessTreeNode` subtree.

        Raises:
            ValueError: If ``pm_node`` uses an unrecognized operator.
        """
        op_map = { Operator.SEQUENCE: "SEQ", Operator.XOR: "XOR", Operator.PARALLEL: "PAR", Operator.LOOP: "LOOP" }
        if pm_node.operator is None:
            name = str(pm_node.label) if pm_node.label else "τ"
            return ProcessTreeNode("LEAF", name=name, frequency=activity_counts.get(name, 0))
        if pm_node.operator not in op_map:
            raise ValueError(f"Unknown operator '{pm_node.operator}'")
            
        op_name = op_map[pm_node.operator]
        custom_children = [DataAssimilation._convert_node(child, activity_counts, binarization_counter) for child in pm_node.children]
        return DataAssimilation._binarize_children(op_name, custom_children, binarization_counter)

    @staticmethod
    def _binarize_children(op_name: str, children: list, binarization_counter: list) -> ProcessTreeNode:
        """
        Fold a list of children into a strict binary subtree for ``op_name``.

        Zero children collapse to a silent (tau) leaf and a single child is
        returned unchanged. Three or more children are right-folded into nested
        binary operators of the same type, incrementing ``binarization_counter``
        for each extra node created.

        Args:
            op_name: Internal operator name (``'SEQ'``, ``'XOR'``, ``'PAR'``,
                ``'LOOP'``) to apply.
            children: The already-converted child nodes to combine.
            binarization_counter: Single-element list used as a mutable counter,
                incremented once per extra binarization node introduced.

        Returns:
            A binary :class:`ProcessTreeNode` representing the combined children.
        """
        if len(children) == 0: return ProcessTreeNode("LEAF", name="empty_tau", frequency=0)
        if len(children) == 1: return children[0]
        if len(children) == 2:
            node = ProcessTreeNode(op_name)
            node.add_child(children[0])
            node.add_child(children[1])
            return node
            
        binarization_counter[0] += 1
        node = ProcessTreeNode(op_name)
        node.add_child(children[0])
        node.add_child(DataAssimilation._binarize_children(op_name, children[1:], binarization_counter))
        return node