import pandas as pd
from pathlib import Path
import xml.etree.ElementTree as ET
import gzip

class LogBatchPreprocessor:
    """
    Batch-converts XES-family event logs into clean, uniform CSV files.

    Parses each ``.xes`` / ``.xml`` / ``.mxml`` / ``.xes.gz`` log directly with
    the standard library XML parser (namespace-agnostic), extracts case ids and
    activity names, injects synthetic per-event timestamps, and writes a CSV with
    the canonical ``case:concept:name`` / ``concept:name`` / ``time:timestamp``
    columns.

    Args:
        input_dir: Directory scanned for input log files.
        output_dir: Directory where converted CSVs are written.

    Attributes:
        input_dir: Path to the input directory.
        output_dir: Path to the output directory.
        valid_extensions: Set of recognized input file extensions.
    """
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.valid_extensions = {'.xes', '.xml', '.mxml', '.xes.gz'} 

    def _strip_namespace(self, tag: str) -> str:
        """
        Strip the XML namespace prefix from a tag.

        Args:
            tag: A possibly namespaced tag (e.g.
                ``'{http://www.xes-standard.org/}trace'``).

        Returns:
            The local tag name (e.g. ``'trace'``).
        """
        return tag.split('}')[-1] if '}' in tag else tag

    def process_single_file(self, file_path: Path) -> bool:
        """
        Convert a single log file to CSV.

        Parses the (optionally gzip-compressed) XML, walks its traces and events
        to collect case ids and activity names with injected monotonic
        timestamps, and writes the resulting DataFrame to a CSV in the output
        directory. Any failure is caught and reported rather than raised.

        Args:
            file_path: Path to the log file to convert.

        Returns:
            ``True`` on success, ``False`` if processing failed.
        """
        print(f"[*] Processing: {file_path.name}")
        try:
            # Route to gzip.open if it's a compressed file
            if file_path.name.lower().endswith('.gz'):
                with gzip.open(file_path, 'rb') as gz_file:
                    tree = ET.parse(gz_file)
            else:
                tree = ET.parse(file_path)
                
            root = tree.getroot()

            data = []
            current_time = pd.Timestamp("2026-01-01 08:00:00", tz="UTC")
            
            # Iterate through all standard XML tags to find traces
            for trace in root:
                if self._strip_namespace(trace.tag) != 'trace':
                    continue
                
                # 1. Extract Case ID
                case_id = "Unknown_Case"
                for child in trace:
                    if self._strip_namespace(child.tag) == 'string' and child.attrib.get('key') == 'concept:name':
                        case_id = child.attrib.get('value')
                        break
                        
                # 2. Extract Events inside the Trace
                for event in trace:
                    if self._strip_namespace(event.tag) != 'event':
                        continue
                    
                    activity = "Unknown_Activity"
                    for child in event:
                        if self._strip_namespace(child.tag) == 'string' and child.attrib.get('key') == 'concept:name':
                            activity = child.attrib.get('value')
                            break
                            
                    # 3. Append to our dataset with the injected timestamp
                    data.append({
                        'case:concept:name': case_id,
                        'concept:name': activity,
                        'time:timestamp': current_time
                    })
                    
                    # Increment time mathematically by 1 minute for sequence preservation
                    current_time += pd.Timedelta(minutes=1)

            # Build the DataFrame manually and save it
            df = pd.DataFrame(data)
            # Remove both extensions for .xes.gz using file_path.name split instead of stem
            clean_name = file_path.name.replace('.xes.gz', '').replace(file_path.suffix, '')
            output_file = self.output_dir / f"{clean_name}.csv"
            
            df.to_csv(output_file, index=False, sep=',')
            
            print(f"    -> 🛠️ Pure XML Extraction successful!")
            print(f"    -> 💾 Saved clean CSV to: {output_file.name} ({len(df)} events)\n")
            
            return True

        except Exception as e:
            print(f"    -> ❌ ERROR processing {file_path.name}: {e}")
            return False

    def run_batch(self):
        """
        Convert every supported log file in the input directory.

        Creates the output directory, discovers all files with a recognized
        extension, converts each via :meth:`process_single_file`, and prints a
        summary of how many succeeded.

        Returns:
            None. Converted CSVs are written to ``output_dir`` and progress is
            printed.
        """
        if not self.input_dir.exists():
            print(f"[FATAL] Input directory does not exist: {self.input_dir.resolve()}")
            return

        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Match on f.name.lower().endswith() rather than f.suffix so .xes.gz is caught
        files_to_process = [
            f for f in self.input_dir.iterdir() 
            if f.is_file() and any(f.name.lower().endswith(ext) for ext in self.valid_extensions)
        ]

        if not files_to_process:
            print(f"[*] No valid log files ({', '.join(self.valid_extensions)}) found in {self.input_dir.resolve()}")
            return

        print(f"[*] Found {len(files_to_process)} log files to process.")
        print("-" * 50)

        success_count = 0
        for file_path in files_to_process:
            if self.process_single_file(file_path):
                success_count += 1

        print("-" * 50)
        print("🎉 Batch Processing Complete!")
        print(f"Successfully converted: {success_count} / {len(files_to_process)} files.")
        print(f"Output Directory:       {self.output_dir.resolve()}")


if __name__ == "__main__":
    
    INPUT_FOLDER = "data/csv/"
    OUTPUT_FOLDER = "data/csv/csv/"
    
    # ==========================================
    
    preprocessor = LogBatchPreprocessor(INPUT_FOLDER, OUTPUT_FOLDER)
    preprocessor.run_batch()