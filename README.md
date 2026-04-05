# EOG-Based Human-Computer Interface (HCI)

## 📌 Project Overview
This project implements a real-time mouse control system using **Electrooculography (EOG)**. [cite_start]By capturing the resting potential of the eye—known as the ocular dipole—the system translates horizontal and vertical eye movements into on-screen cursor coordinates[cite: 89, 90, 91].

## 🛠️ Technical Stack
* [cite_start]**Hardware:** NI USB-6216 DAQ, Bio-instrumentation amplifiers, Surface Electrodes[cite: 164, 165].
* [cite_start]**Software:** Python (PyAutoGUI, NI-DAQmx), MATLAB (Signal Processing & Modeling)[cite: 166, 178].
* [cite_start]**Concepts:** Linear Regression, Ocular Dipole Modeling, Blink Artifact Detection, Signal Conditioning[cite: 57, 106].

## 📈 Key Engineering Achievements

### 1. Mathematical Modeling of Gaze
[cite_start]I developed a linear regression model in MATLAB to map the relationship between eye angle ($\theta$) and recorded voltage ($V$)[cite: 57, 58].
* [cite_start]**Model Equation:** $y = -0.064807x + 0.043008$[cite: 57].
* [cite_start]**Accuracy:** Achieved an $R^{2}$ value of **0.989**, indicating a near-perfect correlation between gaze angle and signal amplitude[cite: 57, 62].

### 2. Signal Acquisition & Hardware Validation
[cite_start]The bio-instrumentation circuit was validated by testing gain against frequency to ensure stability for EOG signals[cite: 163, 164].
* [cite_start]**Stable Gain:** Maintained a consistent gain ($G$) of **56** for frequencies between 1 Hz and 10 Hz[cite: 165].
* [cite_start]**Signal Range:** The system successfully captured horizontal eye movements spanning from **-30° to +30°**[cite: 14].

### 3. Gesture Recognition (Blink-to-Click)
[cite_start]The system distinguishes between intentional saccades and "blink artifacts" to trigger mouse clicks[cite: 104, 106].
* [cite_start]**Algorithm:** Identifies a rapid downward deflection followed by a slow return to the baseline[cite: 106].
* [cite_start]**Implementation:** Successfully demonstrated "closing browser tabs" using only blink detection[cite: 153, 154].

## 💻 Code Logic
The core Python script interfaces with the NI-DAQ to scale voltage inputs into screen pixels based on user-defined sensitivity and polarity:

```python
# From IBEHS4F04_EOG_Mouse.py
Xval = mouse.get_position()[0] + int(Xval) * Xsensitivity * Xpolarity 
Yval = mouse.get_position()[1] + int(Yval) * Ysensitivity * Ypolarity

**🚀 Future Enhancements (Post-Lab)**
To further improve the system's robustness, I am exploring:

Digital Filtering: Implementing a 60Hz Notch Filter to remove power-line interference noted in initial testing.

Adaptive Calibration: Developing a script to dynamically set the Xdeadzone based on the user's resting baseline noise.

Velocity Smoothing: Applying an Exponential Moving Average (EMA) to the cursor movement to reduce jitter from micro-saccades.
