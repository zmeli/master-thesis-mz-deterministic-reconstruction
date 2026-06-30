# BPIC2017 logs — not bundled (size)

The thesis audits seven BPIC2017 event-log variants as part of the curated
111-file evaluation corpus (see `databasis_eval_master.csv`, rows with
`corpus = bpic2017`). They are **omitted from this upload because of their
size** (~1.8 GB combined); the rest of the curated data is bundled directly.

The seven files used, with their on-disk sizes in the working tree:

| file               | size      |
|--------------------|-----------|
| `full-log.xml`     | ~546 MB   |
| `reduced-log.xml`  | ~364 MB   |
| `clustered-log.xml`| ~336 MB   |
| `random-log.xml`   | ~336 MB   |
| `frequency-log.xml`| ~77 MB    |
| `sampled-log.xml`  | ~77 MB    |
| `simulated-log.xml`| ~56 MB    |

These are derived/processed variants of the **BPI Challenge 2017** event log,
which is publicly available from the 4TU.ResearchData repository
(BPI Challenge 2017, DOI: 10.4121/uuid:5f3067df-f10b-45da-b98b-86ae4c7a310b).

Every result the thesis reports for these logs is already captured, per file
and per noise level, in `../../04_results_and_calculations/databasis_eval_master.csv`,
so no number in the thesis depends on having the raw `.xml` files present here.
The original variants live in the working project under `data/BPIC2017/`.
