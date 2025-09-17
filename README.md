# Hand Gesture Volume Control

Control your Windows system volume using hand gestures detected by your webcam!  
This project uses [MediaPipe](https://google.github.io/mediapipe/) for hand tracking and [PyCaw](https://github.com/AndreMiras/PyCaw) for audio control.

---

## Features

- Detects a single hand using your webcam.
- Maps the distance between thumb and index finger to system volume.
- Smooth volume control with adjustable smoothing factor.
- Real-time volume bar visualization.
- Displays distance and volume percentage for easy monitoring.

---

## Requirements

- **Python 3.11+**
- **Windows OS** (PyCaw is Windows-only)
- **Webcam**

### Python Libraries

- `opencv-python`
- `mediapipe`
- `numpy`
- `pycaw`
- `comtypes`

---

## Setup

1. **Navigate to your desired folder:**
   ```powershell
   cd "C:\Users\aaditya\Desktop\Projects"
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/CodeXellius/HandGestureVolumeControl.git
   cd HandGestureVolumeControl
   ```

3. **Create and activate a virtual environment (recommended):**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1   # Windows PowerShell
   ```
   ```bash
   source .venv/bin/activate      # macOS/Linux (not supported by PyCaw)
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the program:**
   ```bash
   python hand_volume_control.py
   ```

2. **Instructions:**
   - Make sure your webcam is connected.
   - Keep your hand visible in front of the camera.
   - Move your thumb and index finger closer or farther apart to decrease or increase volume.
   - Press `q` to quit the program.

---

## How It Works

- **Webcam Capture:** Captures frames from your webcam using OpenCV.
- **Hand Detection:** MediaPipe identifies hand landmarks.
- **Distance Calculation:** Calculates distance between thumb tip (landmark 4) and index tip (landmark 8).
- **Volume Mapping:** Maps the distance to system volume using PyCaw.
- **Visualization:** Displays a real-time volume bar and the numeric volume percentage.

---

## Notes

- Only works on **Windows** due to PyCaw dependency.
- Adjust the `smoothness` variable in the code to change the volume smoothing factor.
- Ensure good lighting for reliable hand detection.

---

## License

MIT License © [AADITYA]
