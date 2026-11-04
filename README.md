# Pupil Response-Based Biometric Authentication

**Undergraduate Thesis Research | Biometric Authentication · Eye Tracking · Human-Computer Interaction · Time-Series Analysis**

## 1. Overview

**Can we identify a person simply by observing how their pupils respond to visual stimuli?**

This question forms the foundation of this undergraduate thesis research.

As Virtual Reality (VR) and Augmented Reality (AR) technologies become increasingly integrated into everyday life, securing personal information and authenticating users has become an important challenge.

Traditional authentication methods, such as passwords, PINs, facial recognition, and fingerprints, have limitations. Passwords can be observed or stolen, while some biometric characteristics may be vulnerable to spoofing attacks.

This research explores an alternative approach: **using involuntary changes in pupil diameter as a biometric characteristic for individual identification.**

Human pupils automatically contract and dilate in response to visual stimuli. Although these responses follow common biological mechanisms, their temporal patterns may differ between individuals.

The central hypothesis of this research is that these individual differences can be measured and potentially used to distinguish legitimate users from impostors.

The primary goal was to investigate the feasibility of pupil-response-based authentication under ordinary indoor conditions.

## 2. Research Objectives

This research addressed three questions:

1. **Individual differences:** Do different people exhibit sufficiently distinct pupil diameter responses when exposed to identical visual stimuli?
2. **Stimulus effectiveness:** Which types of visual stimuli produce pupil responses that are most useful for individual identification?
3. **Authentication feasibility:** Can time-series analysis distinguish legitimate users from impostors using pupil diameter measurements?

To investigate these questions, I developed experimental applications, collected eye-tracking measurements, and implemented a biometric authentication evaluation pipeline using Python.

## 3. Research Methodology

### 3.1 Visual Stimulus Design

I designed eight visual stimuli based on previous research in pupillary light responses, colour perception, eye movements, and visual illusions.

Each stimulus was designed to investigate a different visual factor that could influence pupil diameter.

| Stimulus | Description |
|---|---|
| 1 | Alternating solid-circle colour flicker |
| 2 | Alternating hollow-circle colour flicker |
| 3 | Horizontal eye-tracking movement |
| 4 | Glare illusion using changing colour gradients |
| 5 | Saturation-gradient brightness illusion |
| 6 | Expanding-hole visual illusion |
| 7 | Peripheral-drift motion illusion |
| 8 | Sinusoidal gratings with different orientations |

The stimuli were implemented using **Python and Pygame**, allowing their presentation and timing to be controlled during experiments.

The experimental applications are available in the `Programs/` directory.

### 3.2 Data Collection

Two experiments were conducted using a **Tobii Pro Glasses 2 Eye Tracker** to record participants' pupil diameter changes.

Participants viewed visual stimuli on a 24-inch monitor from approximately 60 cm away in an illuminated indoor environment.

The collected measurements were stored as time-series data for subsequent analysis.

**Experiment 1 — Effects of Stimulus Type and Colour**

The first experiment investigated how stimulus design and colour combinations influenced authentication performance.

- Participants: 6
- Visual stimulus types: 4
- Colour combinations: Red–Blue, Yellow–Blue, Red–Green, Green–Blue
- Total experimental conditions: 16
- Repeated trials: 10 per participant per condition

The objective was to compare identification performance across different stimulus shapes and colour combinations.

**Experiment 2 — Comparison of Eight Visual Stimuli**

The second experiment focused on identifying which visual stimulus was most effective for individual identification.

- Participants: 5
- Visual stimulus types: 8
- Repeated trials: 50 per participant per stimulus
- Total recorded trials: 2,000
- Colour conditions: Standardised where applicable, primarily using Yellow–Blue

Unlike Experiment 1, this experiment focused on differences between stimulus patterns rather than colour combinations.

### 3.3 Data Preprocessing

Eye-tracking measurements may contain missing values or noise caused by blinking, eye movements, and measurement limitations.

Two preprocessing techniques were applied:

**1. Linear Interpolation**

Missing values were reconstructed using linear interpolation, with forward and backward filling applied where necessary.

**2. Low-Pass Filtering**

A low-pass filter with a cutoff frequency of 2 Hz was applied to reduce high-frequency noise while preserving the principal pupil diameter variations.

These steps produced cleaner time-series data for subsequent comparison.

### 3.4 Individual Identification Algorithm

The proposed authentication approach is based on two time-series analysis techniques.

**Dynamic Time Warping Barycenter Averaging (DBA)**

DBA generates a representative time-series waveform from multiple recordings of the same participant.

In this research, each participant's pupil diameter recordings were used to construct a reference waveform for each stimulus condition.

This reference serves as a biometric template representing the participant's typical pupil response.

**Dynamic Time Warping (DTW)**

DTW measures the similarity between two time series while allowing local differences in their timing.

Unlike a simple point-by-point comparison, DTW can align similar response patterns even when their timing varies slightly.

For authentication, the DTW distance was calculated between a recorded pupil response and the registered user's reference waveform.

A smaller DTW distance indicates greater similarity.

**Authentication Procedure**

1. A user observes a predefined visual stimulus.
2. The eye tracker records pupil diameter changes.
3. The recorded time series undergoes preprocessing.
4. DBA generates a reference waveform from the registered user's recordings.
5. DTW measures the distance between a candidate recording and the reference waveform.
6. The distance is compared with a predefined threshold to determine whether the candidate is accepted or rejected.

### 3.5 Performance Evaluation

Authentication performance was evaluated using three metrics:

- **False Acceptance Rate (FAR):** The proportion of impostor attempts incorrectly accepted.
- **False Rejection Rate (FRR):** The proportion of legitimate attempts incorrectly rejected.
- **Equal Error Rate (EER):** The error rate at the operating point where FAR and FRR are equal.

A lower EER indicates better authentication performance.

In both experiments, each participant was evaluated as a legitimate user against recordings from the other participants, who were treated as impostors.

The resulting EER values were averaged across participants for each stimulus condition.

## 4. Research Results

### 4.1 Experiment 1 — Stimulus Type and Colour

The first experiment demonstrated that authentication performance varied depending on the visual stimulus used.

| Visual Stimulus | Average EER |
|---|---:|
| Stimulus 1 — Solid-circle flicker | 0.08 |
| Stimulus 2 — Hollow-circle flicker | 0.11 |
| Stimulus 3 — Horizontal eye tracking | **0.07** |
| Stimulus 4 — Glare illusion | 0.11 |

Stimulus 3 achieved the lowest average EER of **7%**, suggesting that pupil responses associated with horizontal eye-tracking movements may provide useful information for individual identification.

The average EER values across the four colour combinations were:

| Colour Combination | Average EER |
|---|---:|
| Red–Blue | 0.09 |
| Yellow–Blue | 0.09 |
| Red–Green | 0.10 |
| Green–Blue | 0.09 |

These results suggest that, within the investigated conditions, the choice of visual stimulus had a greater influence on identification performance than the choice of colour combination.

### 4.2 Experiment 2 — Comparison of Eight Stimuli

The second experiment extended the investigation to eight types of visual stimuli.

| Visual Stimulus | EER |
|---|---:|
| Stimulus 1 — Solid-circle flicker | 0.21 |
| Stimulus 2 — Hollow-circle flicker | 0.28 |
| Stimulus 3 — Horizontal eye tracking | 0.20 |
| Stimulus 4 — Glare illusion | 0.24 |
| Stimulus 5 — Saturation-gradient illusion | **0.17** |
| Stimulus 6 — Expanding-hole illusion | 0.20 |
| Stimulus 7 — Peripheral-drift illusion | 0.22 |
| Stimulus 8 — Sinusoidal gratings | 0.26 |

Among the eight stimuli, **Stimulus 5 achieved the lowest EER of 17%**, while Stimulus 2 produced the highest EER of 28%.

These findings reinforce the importance of stimulus design in pupil-response-based authentication.

The EER values in Experiment 2 were generally higher than those in Experiment 1. However, the experiments used different participants, trial durations, and experimental conditions, so the results should not be interpreted as a direct comparison of improvements or deterioration in performance.

### 4.3 Key Findings

**1. Pupil diameter responses contain potentially useful individual characteristics.**

The experiments demonstrated that pupil response time series can provide information for distinguishing individuals under the tested conditions.

**2. Visual stimulus design substantially affects identification performance.**

Different stimulus patterns produced different EER values, suggesting that careful stimulus selection is important for developing this authentication approach.

**3. Colour combinations had limited influence within the tested conditions.**

Experiment 1 showed only small differences between the average EER values of the four colour combinations, suggesting that colour selection alone may not substantially improve identification performance.

Overall, the findings support the feasibility of exploring pupil diameter responses as a biometric feature, while also demonstrating that the proposed method requires further improvement before practical deployment.

## 5. Limitations and Future Work

Although the results suggest potential for individual identification, the study has several limitations.

**Authentication accuracy**

The observed EER values remain considerably higher than those achieved by established high-performance biometric authentication systems. Further improvements are needed before the approach can be considered reliable for practical use.

**Limited experimental scale**

Both experiments involved relatively small groups of participants. Additional studies involving more diverse participants, recording sessions, and environmental conditions are necessary to evaluate generalisability.

**Stimulus selection**

The tested stimuli differed in several visual properties. Future research should identify measurable stimulus characteristics and investigate their effects under more strictly controlled conditions.

**User enrolment**

The proposed threshold selection procedure requires reference recordings from other users. An operational system would therefore need a method for establishing authentication thresholds when enrolling its first users.

**Visual stimulus safety**

Some stimuli include flickering patterns that may be unsuitable for individuals with photosensitive epilepsy, migraines, or related sensitivities.

Future work could investigate combinations of multiple sequential visual stimuli, improved feature extraction, and more robust authentication methods to reduce false acceptance and false rejection rates.

## 6. Research Presentation

### Ubiquitous Wearable Workshop (UWW) 2025

This research was presented orally at the **Ubiquitous Wearable Workshop (UWW) 2025**, held at **Kobe University, Japan**.

The workshop was organised by the Tsukamoto–Terada Laboratory at Kobe University, led in part by Professor Masahiko Tsukamoto, together with the NPO Wearable Computer Research and Development Organization.

The oral presentation introduced the research motivation, experimental methodology, proposed pupil-response-based identification method, and evaluation results.

**Workshop:** Ubiquitous Wearable Workshop 2025  
**Venue:** Kobe University, Japan  
**Presentation Type:** Oral Research Presentation  
**Official Website:** https://tt-lab.jp/uww2025/

Related research presentation materials are available in the [`UWW/`](UWW/) directory.

## 7. Repository Structure

This repository contains the experimental applications, recorded data, analysis notebook, evaluation results, and research presentation materials.

```text
.
├── Programs/
│   ├── experiment1.py
│   ├── experiment2.py
│   └── Images/
│
├── Data/
│   ├── Experiment1/
│   │   ├── Participant1/
│   │   └── ...
│   └── Experiment2/
│       ├── Participant1/
│       └── ...
│
├── Data Analysis/
│   ├── analysis.ipynb
│   ├── EER_data.json
│   ├── EER_data_for_experiment2.json
│   └── run.bat
│
├── Dissertation/
└── UWW/
```

| Directory | Contents |
|---|---|
| `Programs/` | Python applications used to present visual stimuli |
| `Data/Experiment1/` | Eye-tracking measurements from Experiment 1 |
| `Data/Experiment2/` | Eye-tracking measurements from Experiment 2 |
| `Data Analysis/` | Data preprocessing, DBA/DTW analysis, and EER evaluation |
| `Dissertation/` | Undergraduate dissertation and related materials |
| `UWW/` | Research presentation materials |

## 8. Running the Project

### Requirements

The original project was developed primarily in a Windows and Python environment.

The following libraries are used:

- pygame
- pandas
- numpy
- matplotlib
- scipy
- dtaidistance
- tslearn
- jupyter

Install the dependencies:

```bash
pip install pygame pandas numpy matplotlib scipy dtaidistance tslearn jupyter
```

### Running the Experimental Applications

To run Experiment 1:

```bash
cd Programs
python experiment1.py
```

To run Experiment 2:

```bash
cd Programs
python experiment2.py
```

Both programs contain interfaces for selecting and presenting the visual stimuli.

Run the scripts from the `Programs/` directory to ensure the relative image paths are resolved correctly.

### Running the Data Analysis

Open the analysis notebook:

```bash
cd "Data Analysis"
jupyter notebook analysis.ipynb
```

Alternatively, on Windows, use the provided `run.bat` launcher, which assumes an existing Conda environment named `timeseries`.

The notebook implements the research analysis pipeline, including:

1. Loading recorded pupil diameter data
2. Linear interpolation and noise filtering
3. DBA reference waveform generation
4. DTW distance computation
5. FAR and FRR evaluation
6. EER calculation and result aggregation

Precomputed EER results are available in:

- `Data Analysis/EER_data.json`
- `Data Analysis/EER_data_for_experiment2.json`

**Reproducibility note:** Some notebook cells contain absolute file paths from the original development environment. These paths must be updated before running the complete analysis on another computer.

The repository includes the experimental software and offline evaluation workflow, rather than a complete production-ready VR authentication system.

## 9. Research Materials

This repository was developed as part of an undergraduate thesis investigating the feasibility of biometric authentication using pupil diameter responses.

The complete dissertation and related research materials are available in the `Dissertation/` directory.

Research presentation materials are available in the `UWW/` directory.

## 10. License

No explicit license is currently included in this repository.
