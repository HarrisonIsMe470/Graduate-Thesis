# Privacy and residual re-identification risk

Pupil-diameter response sequences are the biometric signal studied in this project. A participant number is a pseudonym, not anonymity. The source recordings, spreadsheets, per-participant scores, reference waveforms, and individual plots are therefore not included.

The public copy contains stimulus programs, abstract stimulus images, an archival analysis method, and rounded cohort means. It does not contain names, student numbers, participant mappings, raw or processed human time series, biometric templates, individual scores, consent forms, demographic data, photographs, document authorship metadata, Git history, or original Office/PDF files.

Residual attribution risk remains. An informed person may connect the topic, design, result pattern, UWW 2025 presentation, workshop venue, and distinctive stimuli to a known project. The workshop presentation itself is a public contextual link. Code style, dates described in documentation, and cited experimental details may also support attribution.

Rounded aggregate results are not formally private. The cohorts were small, and no differential-privacy mechanism was applied. Do not treat this repository as evidence that every participant or author is unidentifiable.

If the repository is synchronized publicly:

- synchronize only the contents of this `upload` directory;
- review the final staged file list before committing;
- never add the source `.git` directory, source archive, thesis, decks, spreadsheets, CSVs, notebook checkpoints, or private-data directories;
- keep `PUPIL_DATA_DIR` and `PUPIL_RESULTS_DIR` outside the repository;
- do not publish identity mappings, recruitment records, per-person plots, templates, or exact session metadata;
- obtain appropriate institutional and participant authorization before any release of human-subject data;
- consider a fresh public repository if existing history has ever contained sensitive files.

If a sensitive file is accidentally committed, deleting it in a later commit does not remove it from history. Stop synchronization, rotate any exposed credentials, and use an appropriate history-rewrite and hosting-platform removal process before resuming.
