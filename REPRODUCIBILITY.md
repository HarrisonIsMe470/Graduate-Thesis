# Reproducibility status

This release preserves useful research artifacts while withholding human biometric data. It supports inspection of the stimulus applications, review of the historical analysis code, independent implementation from the documented method, and a synthetic DTW demonstration. It does not support complete reproduction of the reported EER values from public inputs.

## What is available

- The two main stimulus applications and their raster assets.
- Experimental settings notes.
- A sanitized historical notebook containing data segmentation, interpolation, filtering, DBA, DTW, FAR/FRR, and EER logic.
- Rounded cohort-level EER summaries derived from the historical stored score caches.
- A standalone synthetic time-series and DTW demonstration that requires only Python's standard library.

## What is withheld

- Raw CSV and spreadsheet recordings from 11 participant slots across the two experiments.
- Participant-level EER caches, individual plots, and biometric reference waveforms.
- Thesis and presentation files containing personal, academic, photographic, metadata, or biometric information.

## Known historical limitations

The notebook is not a verified `Run All` workflow. Its original Experiment 1 path was absolute and has been replaced. Its original source does not define `preprocess_data_for_experiment1` or `compare_two_participants`, although later cells call them. Some cells are exploratory and assume earlier manual state. The Experiment 1 trial splitter converts data frames to NumPy arrays, while later analysis code expects labeled columns, indicating an unresolved historical inconsistency.

The Experiment 2 preprocessor's loop variable names do not match the declared participant-first data structure, and this release has not silently altered the scientific logic. The third stimulus is handled as 67 stimulus samples while the remaining Experiment 2 stimuli use 100. This may encode the original timing, but it should be checked against the protocol before reuse.

One Experiment 1 stored EER list has seven comparisons while the notebook's aggregate loop uses the first five, consistent with a six-participant comparison design. The public summary follows that implemented aggregation rule. Experiment 2 summaries average the five stored participant values per stimulus.

The Pygame applications and images have been syntax- and asset-checked, but stimulus timing and luminance have not been revalidated on the current machine. Display calibration, monitor characteristics, viewing distance, eye-tracker configuration, room illumination, and operating-system scheduling can affect replication.

## Private authorized rerun

Keep approved data outside the repository. Follow `Data/README.md` for the expected private directory layout, then set:

```bash
export PUPIL_DATA_DIR=/private/path/to/data
export PUPIL_RESULTS_DIR=/private/path/to/results
```

Open `Data Analysis/analysis.ipynb` and review every method assumption before running it. Implement and validate the missing Experiment 1 functions in a separate reviewed branch. Do not treat the stored aggregate summary as a test oracle for altered preprocessing or threshold logic.

For a publication-grade reproduction, preserve a versioned protocol, dependency lock file, hardware and calibration details, ethics/consent constraints, data dictionary, exclusion rules, random seeds, and a participant-independent validation design. None of those should be inferred from this archival release when the source evidence is absent.
