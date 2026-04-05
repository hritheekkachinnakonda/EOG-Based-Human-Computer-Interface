# EOG-Based Human-Computer Interface (HCI)

## 📌 Project Overview
This project implements a real-time mouse control system using **Electrooculography (EOG)**. By capturing the resting potential of the eye—known as the ocular dipole—the system translates horizontal and vertical eye movements into on-screen cursor coordinates.

## 🛠️ Technical Stack
* **Hardware:** NI USB-6216 DAQ, Bio-instrumentation amplifiers, Surface Electrodes.
* **Software:** Python (PyAutoGUI, NI-DAQmx), MATLAB (Signal Processing & Modeling).
* **Concepts:** Linear Regression, Ocular Dipole Modeling, Blink Artifact Detection, Signal Conditioning.

## 📈 Key Engineering Achievements

### 1. Mathematical Modeling of Gaze
I developed a linear regression model in MATLAB to map the relationship between eye angle ($\theta$) and recorded voltage ($V$).
* **Model Equation:** $y = -0.064807x + 0.043008$.
* **Accuracy:** Achieved an $R^{2}$ value of **0.989**, indicating a near-perfect correlation between gaze angle and signal amplitude.

### 2. Signal Acquisition & Hardware Validation
The bio-instrumentation circuit was validated by testing gain against frequency to ensure stability for EOG signals.
* **Stable Gain:** Maintained a consistent gain ($G$) of **56** for frequencies between 1 Hz and 10 Hz.
* **Signal Range:** The system successfully captured horizontal eye movements spanning from **-30° to +30°**.

### 3. Gesture Recognition (Blink-to-Click)
The system distinguishes between intentional saccades and "blink artifacts" to trigger mouse clicks.
* **Algorithm:** Identifies a rapid downward deflection followed by a slow return to the baseline.
* **Implementation:** Successfully demonstrated "closing browser tabs" using only blink detection.

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
