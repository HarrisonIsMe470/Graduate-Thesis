# Pupil Response Based Individual Identification

This anonymized research release preserves the experimental stimulus software, visual assets, analysis method, and cohort-level results from an undergraduate feasibility study. The study asked whether involuntary pupil-diameter responses to controlled visual stimuli contain patterns that may help distinguish individuals.

The release does not contain participant recordings, biometric templates, participant-level results, consent records, a thesis PDF, presentation decks, photographs, or editable design files. Those materials were withheld because removing names alone would not remove the risk of linking a person to a biometric time series. See [PRIVACY.md](PRIVACY.md) and [AUDIT_LOG.md](AUDIT_LOG.md) before sharing or reusing this repository.

## Research questions

The study investigated three questions:

1. Do pupil-diameter response time series differ between people under the tested conditions?
2. Which visual stimulus patterns produced lower authentication error in these small cohorts?
3. Can Dynamic Time Warping based comparisons support a feasibility evaluation of pupil-response identification?

This was an exploratory study with small cohorts. Its results do not establish a deployable authentication system, general population performance, security against attacks, or clinical safety.

## Study design

Two experiments used a Tobii Pro Glasses 2 eye tracker in an illuminated indoor environment. Participants viewed stimuli on a 24-inch display from approximately 60 cm away. The repository preserves the software used to present the stimuli.

Experiment 1 included six participants, four stimulus patterns, four color combinations, and ten repeated trials per condition. The color combinations were red-blue, yellow-blue, red-green, and green-blue.

Experiment 2 included five participants, eight stimulus patterns, and fifty repeated trials per stimulus. Where applicable, the main color condition was standardized to yellow-blue.

The eight stimulus categories were:

| Stimulus | Description |
|---|---|
| 1 | Alternating solid-circle color flicker |
| 2 | Alternating hollow-circle color flicker |
| 3 | Horizontal tracking of moving shapes |
| 4 | Changing color-gradient glare pattern |
| 5 | Saturation-gradient brightness illusion |
| 6 | Expanding-hole illusion |
| 7 | Peripheral-drift illusion |
| 8 | Sinusoidal gratings at several orientations |

Some stimuli flicker or contain high-contrast motion. They may be unsuitable for people with photosensitive epilepsy, migraine, or related sensitivities. The historical software is preserved for research inspection and should not be used with human participants without an appropriate ethics, consent, safety, and data-governance process.

## Analysis method

The original workflow sampled pupil diameter at approximately 50 Hz. Missing left- and right-eye values were linearly interpolated and then filtered with a 2 Hz low-pass filter. Dynamic Time Warping Barycenter Averaging (DBA) produced a reference waveform. Dynamic Time Warping (DTW) measured distances between a candidate waveform and the reference. False acceptance rate, false rejection rate, and equal error rate (EER) were then estimated across tested thresholds.

The historical aggregate values below were recalculated from stored EER caches rather than by rerunning the raw-data pipeline. Values are rounded to two decimals.

| Experiment 1 stimulus | Mean EER |
|---|---:|
| Stimulus 1 | 0.08 |
| Stimulus 2 | 0.11 |
| Stimulus 3 | 0.07 |
| Stimulus 4 | 0.11 |

| Experiment 1 color combination | Mean EER |
|---|---:|
| Red-blue | 0.09 |
| Yellow-blue | 0.09 |
| Red-green | 0.10 |
| Green-blue | 0.09 |

| Experiment 2 stimulus | Mean EER |
|---|---:|
| Stimulus 1 | 0.21 |
| Stimulus 2 | 0.28 |
| Stimulus 3 | 0.20 |
| Stimulus 4 | 0.24 |
| Stimulus 5 | 0.17 |
| Stimulus 6 | 0.20 |
| Stimulus 7 | 0.22 |
| Stimulus 8 | 0.26 |

Stimulus 3 had the lowest mean EER in Experiment 1, and Stimulus 5 had the lowest mean EER in Experiment 2. The cohorts and experimental conditions differed, so the two experiments should not be treated as a before-and-after comparison. The sample sizes were too small to support broad performance claims.

The exact rounded summary and its calculation notes are in [`results/aggregate_eer.json`](results/aggregate_eer.json).

## UWW 2025 oral presentation

This research was presented orally at the [Ubiquitous Wearable Workshop 2025](https://tt-lab.jp/uww2025/) at Kobe University on 19-20 December 2025. The workshop was organized by Kobe University's Tsukamoto-Terada Laboratory, associated with Professor Masahiko Tsukamoto, together with the NPO Wearable Computer Research and Development Organization.

The original UWW deck, draft script, media, editable graphics, and source images are not distributed in this release because they contained document metadata, identifiable photographs, participant-derived plots, or layered source material. [`UWW/README.md`](UWW/README.md) preserves an anonymous summary.

## Repository contents

```text
.
├── Programs/
│   ├── experiment1.py
│   ├── experiment2.py
│   ├── experiment1_settings.txt
│   ├── experiment2_settings.txt
│   └── Images/
├── Data/
│   └── README.md
├── Data Analysis/
│   └── analysis.ipynb
├── results/
│   └── aggregate_eer.json
├── audit/
│   ├── source_manifest.json
│   └── image_metadata_log.json
├── synthetic_demo.py
├── REPRODUCIBILITY.md
├── PRIVACY.md
└── AUDIT_LOG.md
```

The `Programs` directory contains the two Pygame stimulus applications and 68 raster stimulus assets. Path strings were made portable and one mislabeled JPEG was converted to a real PNG. Image pixels were retained; ancillary metadata was removed.

The notebook is a sanitized historical method reference. It contains known gaps and cannot reproduce the reported results without authorized private data and additional repair. Read [REPRODUCIBILITY.md](REPRODUCIBILITY.md) before running it.

## Running the stimulus software

Use Python 3 and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run either application from the repository root:

```bash
python Programs/experiment1.py
python Programs/experiment2.py
```

The software was developed for a Windows-based experimental setup. The copied image paths now use portable separators, but display timing and appearance have not been revalidated on other operating systems or monitors.

## Safe analysis demonstration

The repository contains a small deterministic demonstration that creates synthetic time series and computes DTW distances without loading any human data:

```bash
python synthetic_demo.py
```

This checks only that the included example logic runs. Its artificial output is not a research result and cannot validate the accuracy of the historical analysis.

For separately authorized private data, follow [`Data/README.md`](Data/README.md). Keep the data outside this public repository and set `PUPIL_DATA_DIR` and `PUPIL_RESULTS_DIR` to private locations.

## Sharing and reuse

No license was present in the source repository, and none has been invented for this copy. Public visibility does not itself grant reuse rights. Confirm ownership of code, text, images, and any cited third-party material before distributing or licensing the release.

The audit reduces obvious disclosure risk but cannot prove anonymity. The research topic, distinctive stimulus collection, dates, workshop record, method, and aggregate results may still allow an informed person to infer the project or its author. Do not combine this release with private participant records, identity keys, recruitment records, or per-person results.
