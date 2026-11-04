# Anonymization audit log

## Scope and method

The audit covered 450 files in the source working tree and the complete local Git metadata directory. It inspected readable text, Python code, Jupyter notebooks, CSV schemas and values, spreadsheet package metadata, Office and OpenDocument package metadata and embedded media, the thesis PDF text and metadata, filenames, archives, raster metadata, and common absolute-path and identity patterns.

This release was built from an explicit allowlist. Files were copied only when they were needed to preserve the stimulus software, stimulus assets, method reference, or aggregate results. The source directory was not edited. No commit, push, remote change, or network upload was performed.

The machine-readable [`audit/source_manifest.json`](audit/source_manifest.json) records a disposition for each of the 450 source working-tree files. Identifying thesis and bundle filenames are masked in that public manifest. The 507 files inside `.git` are represented as one excluded category because publishing individual Git objects or hashes could disclose removed history.

## Retained and sanitized

- Two main Pygame experiment applications were retained. Windows image separators were changed to portable separators. No authorship banner or embedded username was found in the retained files.
- Sixty-eight stimulus images were retained. PNG ancillary metadata was removed while retaining pixels and essential color/transparency chunks. One file with a `.png` name was actually JPEG data; it was decoded and saved as a real metadata-free PNG.
- Two experimental settings text files were retained under simpler names.
- The analysis notebook was retained as an archival method reference. Three saved output objects, all execution counts, cell metadata, attachments, kernel version details, and original absolute paths were removed. Paths now use environment variables and local private-data placeholders.
- Original per-participant EER cache arrays were replaced by two-decimal cohort means in `results/aggregate_eer.json`.

## Excluded

- All raw CSV and spreadsheet recordings. The source held 64 CSVs and 67 spreadsheets, including backups. CSVs contained timestamps and left/right pupil diameter values. Spreadsheet metadata in many files exposed an editor name.
- The thesis PDF. Its cover exposed a personal name and student number; later pages included participant-derived figures. The PDF metadata itself did not contain an author name, but this did not make the document anonymous.
- Dissertation and UWW presentation decks. Package metadata exposed author/editor names, and embedded media included an experiment photograph and individual pupil-response plots.
- The UWW draft script, presentation media, editable OpenDocument drawings, Photoshop and GIMP sources, EPS exports, and redundant JPEGs. These were replaced by a plain anonymous summary.
- A research archive and a duplicate research bundle. They contained copies of identifiable or privacy-sensitive materials and would have bypassed file-level sanitation.
- Notebook checkpoints. They contained large cached outputs and duplicated historical code.
- Old program backups, compiled Python bytecode, ad hoc image conversion scripts, system files, shell history, and machine-specific launchers.
- The entire `.git` directory, including commit history, object data, references, logs, configuration, and remote information.

## Findings that affected the release

- Participant labels were numeric, but the measurements are the biometric feature being evaluated. Renaming participant folders would not adequately anonymize the signals.
- No emails, API tokens, passwords, or GitHub URLs were found in the retained plain-text code and documentation scan.
- The retained stimulus images showed abstract colored shapes and illusions. Source presentation media also included a hand/device experiment photograph and participant plots, so presentation and thesis images were not reused.
- The analysis notebook contained an absolute Windows development path. It now uses `PUPIL_DATA_DIR` and `PUPIL_RESULTS_DIR`.
- One Experiment 1 stored score list contained seven comparisons while the historical notebook logic used five. Aggregate values in the release follow the notebook's first-five comparison behavior, and the inconsistency is disclosed.

## Verification performed

- Re-scanned all released filenames and text-bearing files for the known personal identifiers, student number, usernames, absolute paths, email addresses, credentials, and source repository path.
- Inspected the released notebook as JSON to confirm zero saved outputs, zero execution counts, no attachments, and no original absolute path.
- Parsed every released Python file and compiled the notebook code cells for syntax.
- Decoded every released image and checked that its stored format matches PNG.
- Ran the synthetic demonstration and checked deterministic expected output.
- Compared a pre-build source snapshot after completion to confirm that no source file changed.

## Residual risk

The release is pseudonymous, not provably anonymous. The combination of research topic, experimental design, unusual stimulus assets, aggregate results, workshop date and venue, and public presentation record may let an informed person infer the project or author. Source code style and historical implementation details can also contribute to attribution.

The rounded cohort means are less identifying than per-person scores, but rounding is not differential privacy. Small cohorts increase inference risk. Do not add per-participant results, waveforms, photos, demographic details, exact recruitment context, consent forms, or identity mappings to a public copy.

The audit cannot establish copyright ownership, participant consent for public release, ethics approval conditions, or a legal basis for sharing. Those questions require the original project records and institutional review. No license has been added.
