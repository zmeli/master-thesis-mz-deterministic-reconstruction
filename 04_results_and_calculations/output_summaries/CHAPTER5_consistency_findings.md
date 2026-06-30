---
status: OPEN — findings recorded, fixes not yet applied to the chapter
found: final consistency pass requested before starting the tau/XOR bug fix
---

# Chapter 5 consistency findings (pending fix)

Findings from a review pass over the chapter draft as assembled so far (5.0
through the start of 5.4.3's "Relation to the Research Question" — the rest of
the chapter, 5.5/5.6, was not visible in that pass and still needs the same
check). Each item includes the exact replacement text already drafted.

## 1. Stray TODO left inside body text (Data Exposure, "ST-only" paragraph)

Original ends with: "...the set of patterns behind the number is now smaller and
more specific. **TODO Explain why we have this when it probably will stay at 100
every time.**"

Replacement:
```latex
Still $100\%$ on this tree, since $A$ and $D$ happen to be fully confirmed on their own -- but the set of patterns behind the number is now smaller and more specific. This variant earns its place even though it often reads $100\%$: it is the one number that isolates whether a confirmation failure sits in the engine's \emph{strict} claims specifically, rather than in its AS-tagged or internal ones. Every Data Exposure dip found in this evaluation traced back to AS or internal content (Section~\ref{sec:baseline-values}) -- ST-only stayed at $100\%$ throughout. That is not a coincidence the metric reports passively; it is the check that rules out the more serious possibility every time it holds.
```

## 2. Chapter intro misdescribes its own structure

Original: "Section~\ref{sec:exposure-metrics} itself now also hosts the
noise-filtering paradox and the operator-driven correlation analysis **as
subsections** rather than standalone topics..." — factually wrong; 5.5/5.6 are
top-level `\subsection`s, siblings of 5.4, not nested inside it.

Replacement:
```latex
Section~\ref{sec:noise-paradox} and Section~\ref{sec:operator-vulnerability} then apply these same exposure metrics through two specific lenses -- noise filtering's effect on the model/data match, and the relationship between operator composition and exposure -- rather than introducing separate phenomena of their own.
```

## 3. Two leftover "fake ref + TODO" artifacts

Same bug pattern already fixed once in the tau/XOR paragraph, missed here:

- 5.2: `Section~\ref{sec:choice-starvation} \textit{(TODO REF: Ch.~3, Choice Starvation)}`
  → `\textit{(TODO REF: Ch.~3, Choice Starvation)}`
- 5.4.2 intro: `(Section~\ref{sec:behavioral-forcing} \textit{(TODO REF: Ch.~3, Section 3.1)})`
  → `\textit{(TODO REF: Ch.~3, Section 3.1, Behavioral Forcing)}`

`sec:choice-starvation` and `sec:behavioral-forcing` are not real labels anywhere
in this chapter; citing them alongside a TODO is contradictory (looks resolved,
is actually broken).

## 4. First paragraph cites an unconfirmed label with no TODO flag

`Chapter~\ref{sec:theoretical-framework}` (in the opening paragraph) was never
confirmed to exist in the actual Chapter 3 source, unlike every other Chapter 3/4
reference, which is flagged. Either confirm the label is real, or flag it the same
way:
```latex
Chapter~\ref{sec:theoretical-framework} \textit{(TODO: confirm this label exists in Ch.~3)}
```

## 5. 5.1's measure list omits Data Coverage entirely

Section 5.1 is the complete inventory of measures used in the chapter, but
Data Coverage (all of Section~\ref{sec:data-coverage}) is missing. Add, parallel
to the existing Data Exposure bullet:
```latex
\item \textbf{Average Data Coverage in \%}: Mean of the recall-side counterpart to Data Exposure -- how much of the real log's content, rather than how much of the engine's claims, is explained by VERIFIED patterns, split the same way into \emph{ST-only}, \emph{ST + ST-in-PAR}, and \emph{Total} (Section~\ref{sec:data-coverage}).
```

## 6. Tree ordering inconsistent between bullet list and tables (5.4.3)

The "Four Trees" bullets list them as $T_{\text{simple}}, T_{\text{run}},
T_{\text{discrepancy}}, \text{PDC2021}$, but both tables order columns as
$T_{\text{simple}}, T_{\text{run}}, \text{PDC2021}, T_{\text{discrepancy}}$. The
discussion paragraph right after ("the third and fourth trees...") only reads
correctly under the table's ordering. Fix: reorder the bullet list to match the
tables:
```latex
\begin{itemize}
    \item \textbf{$T_{\text{simple}}$} (\texttt{test\_02\_seq\_xor.csv}, synthetic): no PAR or LOOP operators. $\rightarrow(A,\ \times(C,B),\ D)$, $N=34$.
    \item \textbf{$T_{\text{run}}$} (\texttt{test\_27\_par\_loop\_noxor.csv}, synthetic): the tree used throughout Section~\ref{sec:tree-exposure}. $\rightarrow(A,\ +(\circlearrowleft(B,C),\ D),\ E)$, $N=20$.
    \item \textbf{PDC2021} (\texttt{pdc2021\_0000000.xes}, real, unfiltered): a 70-activity tree, too large to reproduce in full here. Its shallow structure is dominated by Sequence and Exclusive Choice -- but several PAR blocks sit deep inside it, e.g.\ $\rightarrow(t24,\ +(t23,\,t29),\ t25,\ t26,\ t27)$, one of a handful of similar Parallel fragments buried throughout the tree.
    \item \textbf{$T_{\text{discrepancy}}$} (\texttt{test\_15\_loop3.csv}, synthetic): despite its tiny case volume, the tree is three Loop-levels deep, with a Parallel block sitting directly inside the outer Loop's body and a second, independent Loop nested inside one of that Parallel block's own branches. $\rightarrow\bigl(A,\ \circlearrowleft(+(\,\times(\tau,G),\ [\text{3 further nested LOOP/XOR/PAR levels}]\,),\ H)\bigr)$, $N=5$.
\end{itemize}
```

## 7. Stale file count in a TODO note (5.3)

`(TODO: the full 28/29-file stress-test corpus does not yet have a dedicated
results table...)` — every other reference in the chapter says 29 files
consistently (the data dir has sample_log.csv + 27 numbered tests, with
`test_10` used twice, giving 1 + 28 = 29). Fix:
```latex
\textit{(TODO: the full 29-file stress-test corpus does not yet have a dedicated results table in the Appendix -- add one before citing "full results... listed in Appendix" anywhere in this chapter.)}
```

## Not yet checked

Sections 5.5 (Paradox of Noise Filtering) and 5.6 (Operator-Driven Vulnerability)
were not visible in the pass that produced this list — the same fake-ref+TODO
artifact was already found and fixed once in 5.5's tau/XOR paragraph earlier in
the session, but that fix's presence in the current master copy hasn't been
re-confirmed. Re-check both sections the same way once assembled.
