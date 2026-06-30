# Thesis Update Package: Tree Exposure Redefinition

This file replaces the earlier draft of the same name. It is written to drop directly
into Section 5.4.2 ("Tree Exposure (Tree-Side KPI)") and the surrounding subsections
of the actual thesis document (`Expose_WS25-15.pdf` content), matching its existing
notation ($\rightarrow, \times, \wedge, \circlearrowleft, \tau$, $\langle\cdot\rangle$
for ordered traces, $\{\cdot\}$ for Activity Sets, the `Where:` glossary convention,
and the worked-example style already used in 5.4.2).

It incorporates the **final** corrected `fragment_strict_exposure()` definition:
candidates are pulled *only* from the engine's Full/Prefix/Suffix root partition --
never from fragments tagged `(in PAR_x)`/`(in LOOP_x)`, since a fragment trapped
inside an opaque block is only locally known relative to its own branch, not
globally. (An intermediate version of this metric credited those internal
fragments too; that version is not used anywhere below.)

---

## 0. Checklist of everything that needs updating in the thesis

1. **Section 5.4.2, "Tree Exposure (Tree-Side KPI)"** -- the core definition and its
   `Where:` glossary currently say $\mathcal{F}$ contains *both* Strict Traces and
   Activity Sets undifferentiated. This is the central fix: replace with the
   five-way decomposition in Part 1 below.
2. **Section 5.4.2's worked example** ("Example: Tree Exposure on a Sequential
   Choice", $T = \rightarrow(\times(A{:}6,B{:}4), \times(C{:}8,D{:}2))$) -- **no
   change needed**. That tree has no PAR/LOOP, so End-to-End Tree Exposure = Total
   Forced Volume = 60% already; the existing derivation is still exactly correct
   under the new definition. Worth a one-sentence note confirming this, see Part 1.
3. **Section 5.3, Table 2** (`test_27_par_loop_noxor.csv` worked example) -- the
   row "Tree Exposure: 100.00%" is now misleading; replace with Part 2 below.
4. **Section 5.4.2, "Quantifying Exposure: Fractional Companion Metrics"** -- the
   PDC2021 example citing "Tree Exposure for that file came out to 0.1%" needs the
   same five-way breakdown computed for that specific file before it can be quoted
   under the new definition (flagged in Part 4 -- requires a fresh audit run, the
   number is not recomputed in this package).
5. **Section 5.4.2, "Reading the Four Metrics Together" table** -- add a row for
   Fragment-Level Strict and split the Tree Exposure row; see Part 3.
6. **Section 5.4.3, "Observed Baseline Values Data vs. Tree Exposure", Table 4** --
   the `test_18_inter_loop.csv` row (33.33% Tree Exposure) is from before this
   redefinition; needs re-stating as Total Forced Volume, with End-to-End/Fragment
   columns added if the table is to stay informative. Requires re-audit (flagged,
   not computed here).
7. **Section 5.6, "Operator-Driven Vulnerability"** -- this section's correlation
   analysis was computed against the old, undifferentiated Tree Exposure. The
   sentence "theoretical Tree Exposure showed no statistically significant
   correlation with any specific operator share" should be re-validated once the
   correlation is recomputed against End-to-End Tree Exposure specifically, since
   that number is now far more sensitive to PAR/LOOP presence than the old one was
   -- it would be surprising if the correlation stayed insignificant. Flagged, not
   recomputed here (requires the PDC2021 batch re-audit).
8. **Section 7.3, "Future Research Directions"** -- the scribbled note "everythin
   in a PAAR are technically found but we do not know the concrete flow of them...
   not in which order" is exactly the insight this redefinition implements. Remove
   it from Future Research and fold it into the Section 5.4.2 redefinition instead
   (it's now a contribution, not an open question) -- see Part 1's framing.
9. **Appendix (Section 8), Table 5** -- no change. The 64-permutation matrix
   classifies ST-only vs. Mixed at the level Behavioral Forcing already defines in
   Section 3.1; it is unaffected by how Tree Exposure aggregates volume.

---

## Part 1: Section 5.4.2 redefinition

Replace the paragraph beginning "As defined $N$ denotes the global root-level
frequency..." through the end of the "Example: Tree Exposure on a Sequential
Choice" subsection with the following.

```latex
As defined, $N$ denotes the global root-level frequency of the process tree, and
$\mathcal{F}$ denotes the set of forced patterns returned strictly by the
Deterministic Engine's Full state partition (Section 4.5.2). Earlier in this thesis,
$\mathcal{F}$ was treated as a single undifferentiated pool of Strict Traces and
Activity Sets. Two findings, both confirmed directly against the implemented engine,
make that treatment too coarse for a thesis whose stated goal (Section 1.2) is
\emph{control-flow} reconstruction specifically:

\begin{enumerate}
    \item The Block Locking mechanism's Sequence rule (Section 4.5.2) tags every
    cross-multiplied chain as a Strict Trace regardless of its components. A chain
    that sequentially absorbs an opaque \texttt{[nested PAR\_k]} or
    \texttt{[nested LOOP\_k]} placeholder is therefore still labelled \texttt{[ST]}
    -- confirmed on \texttt{test\_20\_loopDouble.csv}, whose sole Full-bucket entry,
    $\langle A, \text{[nested PAR\_1]}, G \rangle$, carries the \texttt{[ST]} tag
    despite containing an unresolved Parallel block. The tag alone therefore cannot
    distinguish a chain whose order is fully known from one that merely has a
    fully known \emph{skeleton} around an opaque island.
    \item Crediting every element of $\mathcal{F}$ equally, regardless of whether it
    is a Strict Trace or an Activity Set, conflates two different claims: that a
    case's content is fully ordered, and that a case's content is merely
    accounted-for as a set. Recall from Section 3.1 that an Activity Set already
    concedes chronological order is unknown by definition -- crediting it identically
    to a Strict Trace overstates how much control flow has actually been
    reconstructed.
\end{enumerate}

Tree Exposure is therefore reported as a five-way decomposition rather than a single
percentage. Let $\mathcal{F}_{\text{ST}} \subseteq \mathcal{F}$ be the subset of
patterns that are \emph{globally strict} -- containing no embedded
\texttt{[nested $\cdot$]} placeholder anywhere in their structure, checked
structurally rather than by trusting the \texttt{[ST]}/\texttt{[AS]} tag -- and let
$\mathcal{F}_{\text{AS}} = \mathcal{F} \setminus \mathcal{F}_{\text{ST}}$ be the
remainder. $\mathcal{F}_{\text{AS}}$ is further split by checking, for every
opaque block referenced inside a pattern, whether that block's own children
independently resolve to pure Strict Traces (its branches are individually
deterministic; only the cross-branch interleaving, or a Loop's redo count, remains
open) -- call this resolvable subset $\mathcal{F}_{\text{AS-res}}$, with
$\mathcal{F}_{\text{AS-opq}} = \mathcal{F}_{\text{AS}} \setminus
\mathcal{F}_{\text{AS-res}}$ the genuinely irreducible remainder.

\textbf{Tree Exposure (End-to-End)}, the new headline number, credits only
$\mathcal{F}_{\text{ST}}$:

\[
\text{Tree Exposure (End-to-End)} \;=\; \frac{\sum_{(n,f,t)\,\in\,\mathcal{F}_{\text{ST}}} f}{N} \times 100\%
\]

\textbf{Total Forced Volume} preserves the original, pre-redefinition formula
exactly, summing over all of $\mathcal{F}$:

\[
\text{Total Forced Volume} \;=\; \frac{\sum_{(n,f,t)\,\in\,\mathcal{F}} f}{N} \times 100\%
\]

\textbf{AS-Resolved} and \textbf{AS-Opaque} are defined analogously over
$\mathcal{F}_{\text{AS-res}}$ and $\mathcal{F}_{\text{AS-opq}}$ respectively. By
construction,
$\text{End-to-End} + \text{AS-Resolved} + \text{AS-Opaque} = \text{Total Forced
Volume}$ -- so every Tree Exposure figure already reported elsewhere in this thesis
remains correct and citable under the \emph{Total Forced Volume} name; nothing is
retracted, only decomposed into how much of that volume is actually order-known.

\textbf{Where:}
\begin{itemize}
    \item $N$ -- the global root-level case frequency of the process tree.
    \item $\mathcal{F}$ -- the engine's Full-state partition: Strict Traces and
    Activity Sets that together form a non-redundant, end-to-end account of a case.
    \item $\mathcal{F}_{\text{ST}}$ -- the subset of $\mathcal{F}$ containing zero
    embedded opaque placeholders anywhere in their structure: cases whose order is
    \emph{entirely} known, start to finish.
    \item $\mathcal{F}_{\text{AS-res}}$ -- the subset of $\mathcal{F}\setminus
    \mathcal{F}_{\text{ST}}$ whose referenced opaque block(s) independently resolve
    to pure Strict Traces internally; only the block's own boundary (a Parallel
    interleaving, or a Loop's redo count) remains unknown.
    \item $\mathcal{F}_{\text{AS-opq}}$ -- the remainder: patterns referencing at
    least one opaque block that does not resolve even internally.
\end{itemize}

\paragraph{Example: Tree Exposure on a Sequential Choice (unchanged).} The
worked example $T = \rightarrow(\times(A{:}6,B{:}4), \times(C{:}8,D{:}2))$, $N=10$,
requires no correction under this redefinition: because the tree contains neither a
Parallel nor a Loop operator, every pattern in $\mathcal{F}$ is automatically
globally strict, so $\mathcal{F} = \mathcal{F}_{\text{ST}}$ and End-to-End Tree
Exposure equals Total Forced Volume equals the already-derived 60\%. The
decomposition only changes results for trees containing PAR or LOOP, illustrated
next.

\paragraph{Tree Exposure (Fragment-Level), a complementary metric.} End-to-End Tree
Exposure is all-or-nothing per case: the entire case must be one known chain to
contribute anything. A second, complementary number generalizes the strict
standard down to the fragment level, mirroring how Max and Avg (below) generalize
the binary Full-or-nothing credit into partial credit -- but restricted to
fragments that are themselves globally strict. Candidates are pulled only from the
engine's Full, Prefix, and Suffix root-partition buckets (Section 4.5.2); fragments
harvested from \emph{inside} an opaque PAR or LOOP block -- tagged
$(\text{in PAR}_k)$ or $(\text{in LOOP}_k)$ -- are deliberately excluded even when
individually deterministic, since such a fragment's position is only known relative
to its own branch, not globally: it does not qualify as something we can say will
appear in a specific, fully knowable position. Only fragments that sit outside every
opaque wrapper qualify, whether they span the whole case or only part of it.
```

## Part 2: Section 5.3, corrected `test_27_par_loop_noxor.csv` worked example

Replace Table 2 and its surrounding sentence with the following (mined structure,
the two nested-block descriptions, and the "ten patterns verify exactly" sentence
in Section 5.3 are all still correct and need no change -- only the metrics
paragraph and table change).

```latex
Table 2 summarizes the outcome under the Tree Exposure redefinition introduced in
Section 5.4.2: all ten patterns still verify exactly, with zero Discrepancy and
zero Ghost Patterns, and the case's entire volume is still fully accounted for
(100\% Total Forced Volume). However, the engine's only Full-bucket pattern,
$\langle A, \text{[nested PAR\_1]}, E \rangle$, contains an embedded opaque
placeholder despite carrying an \texttt{[ST]} tag, so End-to-End Tree Exposure is
0\%: the case's order is not actually known start to finish. Checking
\texttt{PAR\_1} itself shows it does not resolve internally either -- its LOOP
branch carries a nonzero redo count, an irreducible question (how many times did
this case redo?) -- so the entire 100\% lands in AS-Opaque, none of it in
AS-Resolved. Fragment-Level Tree Exposure is 14.93\%, contributed entirely by the
bare $A$ and $E$ activities that sit outside \texttt{PAR\_1}; nothing trapped
inside the Parallel block contributes, since Fragment-Level credit excludes any
fragment only locally known within an opaque block. This revises the example's
takeaway: the engine resolves the LOOP/PAR interaction \emph{soundly} -- zero
Discrepancy, zero Ghost, full volume accounted for, without relying on XOR's
Activity-Set escape valve -- but this file does not demonstrate that the resulting
case order is known, which it explicitly is not.

\begin{table}[h]
\centering
\caption{Worked example: \texttt{test\_27\_par\_loop\_noxor.csv}, under the
redefined Tree Exposure}
\begin{tabular}{ll}
\hline
\textbf{Metric} & \textbf{Value} \\
\hline
Mined structure & $\rightarrow (A, +(\circlearrowleft (B, C), D), E)$ \\
Operators present & SEQ, PAR, LOOP (no XOR) \\
Verified Patterns & 10 / 10 \\
Discrepancy / Ghost Patterns & 0 / 0 \\
Tree Exposure (End-to-End) & 0.00\% \\
Tree Exposure (Fragment-Level) & 14.93\% \\
Total Forced Volume & 100.00\% \\
AS-Resolved / AS-Opaque & 0.00\% / 100.00\% \\
Data Exposure & 100.00\% \\
Mean Absolute Exposure Volume & 6.70 events/case \\
\hline
\end{tabular}
\end{table}

Every other LOOP+PAR file in the stress-test corpus also contained an Exclusive
Choice, so none of them alone could rule out XOR's Activity-Set escape valve as the
reason LOOP+PAR resolved correctly elsewhere -- this file (and its mirror-direction
companion, \texttt{test\_26\_loop\_par\_noxor.csv}, which scores nearly identically:
0\% End-to-End, 100\% Total Forced, 14.0\% Fragment-Level, fully AS-Opaque) closes
that gap, with the caveat above about what "resolved" does and does not claim.
```

## Part 3: Section 5.4.2, "Reading the Metrics Together" table

Add a row for Fragment-Level Strict immediately below Tree Exposure, and rename the
existing Tree Exposure row to make clear it is now the End-to-End variant:

```latex
\begin{table}[h]
\centering
\begin{tabular}{p{2.6cm}p{4cm}p{4cm}p{4cm}}
\hline
\textbf{Metric} & \textbf{Answers} & \textbf{Strength} & \textbf{Limitation} \\
\hline
Tree Exposure (End-to-End) & Is the entire case, start to finish, one known order? &
Strict, unambiguous, order-only guarantee & All-or-nothing; zeroes out on any
blocking Loop/Parallel, even a fully-resolved one \\
Tree Exposure (Fragment-Level) & Is \emph{any} part of the case known in a fully
knowable position? & Recovers partial order information End-to-End discards &
Still excludes anything trapped inside an opaque block by design \\
Max & \% known vs.\ worst-case length & Conservative lower bound & Can be
uninformatively small for degenerate Loops \\
Avg & \% known vs.\ typical length & Realistic, reacts smoothly to partial ambiguity
& Still relative; hides absolute content volume \\
Mean & Real events known per case (absolute) & Comparable across model sizes; no
Loop-bound assumption needed & Inherits existence-only Loop semantics at face value \\
\hline
\end{tabular}
\end{table}
```

Note that Max, Avg, and Mean are deliberately left unchanged by this redefinition --
they answer a length/volume question ("how much expected case content is known"),
not an order-certainty question, and should not be read as implying the same
order-determinism standard as the redefined Tree Exposure.

## Part 4: Outstanding re-computations (not done in this package)

The following numbers in the thesis were computed under the old, undifferentiated
Tree Exposure and need a fresh audit run before being re-quoted under the new
five-way decomposition:

- Section 5.4.2's PDC2021 example (Tree Exposure "0.1%" on the root-Loop-dominated
  file) -- needs the End-to-End/Fragment-Level/Total-Forced/AS-Resolved/AS-Opaque
  breakdown for that specific file.
- Section 5.4.3, Table 4 (`pdc2021_0000000.xes`, `test_18_inter_loop.csv`).
- Section 5.6's correlation analysis between operator share and Tree Exposure --
  should be recomputed against End-to-End Tree Exposure specifically, since it is
  expected to correlate far more strongly with PAR/LOOP presence than the old,
  undifferentiated number did.

All three require re-running the BPIC2021/PDC2021 batch through the patched
`auto_verifier_v2.py`, which was explicitly deferred (not executed) when this fix
was implemented, due to its cost relative to the 28-file stress corpus.
