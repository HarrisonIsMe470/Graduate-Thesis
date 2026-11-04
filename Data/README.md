# Participant data withheld

The source contains 64 CSV recordings and 67 spreadsheet files, including backups. These are excluded. The CSVs expose three columns: `Recording timestamp`, `Pupil diameter left`, and `Pupil diameter right`. Nonempty CSV observations were numeric in the audit, but pupil responses are the biometric signal studied for identification. Participant numbers do not make these recordings anonymous.

The schema is retained for independently authorized replication:

| Column | Interpretation |
|---|---|
| Recording timestamp | Millisecond recording time; code expects approximately 20 ms sampling intervals |
| Pupil diameter left | Left pupil diameter in mm; missing values may occur |
| Pupil diameter right | Right pupil diameter in mm; missing values may occur |

For private use, set `PUPIL_DATA_DIR` to a separate data directory containing `Experiment1/Participant1/E1.csv` through six participants and four stimuli, and `Experiment2/Participant1/Stimulus1.csv` through five participants and eight stimuli. These are required layout placeholders, not an identity mapping. The loader accepts `.csv` and `.CSV` without depending on filesystem case insensitivity. Set `PUPIL_RESULTS_DIR` separately for private derived results.

Experiment 1 splits conditions at timestamp discontinuities. Experiment 2 assumes 50 trials, 50 Hz and 2 s preparation; its third stimulus uses 67 stimulus samples, while others use 100. These are legacy implementation assumptions, not a guarantee that arbitrary input data meet the design. Read `REPRODUCIBILITY.md` before reuse.

No identity key, demographic table, human waveform, real-data example row, or per-participant score is distributed. The standalone synthetic demonstration generates artificial values from fixed mathematical functions without reading original data.
