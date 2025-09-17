# Hand Gesture Volume Control

Control your system volume using hand gestures with your webcam! This project uses MediaPipe to detect hand landmarks and PyCaw to control Windows audio volume based on the distance between your thumb and index finger.

# Features

Detects a single hand using your webcam.

Maps the distance between thumb and index finger to system volume.

Smooth volume control with adjustable smoothing factor.

Real-time volume bar visualization on the screen.

Displays distance and volume percentage for easy monitoring.

# Requirements

Python 3.11+

# Libraries:

opencv-python

mediapipe

numpy

pycaw

comtypes

# Install dependencies via:

pip install -r requirements.txt

# Setup

Clone the repository:

git clone https://github.com/your-username/HandGestureVolumeControl.git
cd HandGestureVolumeControl


Create and activate a virtual environment (optional but recommended):

python -m venv .venv

Windows
.\.venv\Scripts\Activate.ps1

macOS/Linux
source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt

Usage

# Run the program:

python hand_volume_control.py


Make sure your webcam is connected.

Keep your hand visible in front of the camera.

Move your thumb and index finger closer or farther apart to decrease or increase volume.

Press 'q' to quit the program.

# How it Works

Webcam Capture: Captures frames from your webcam using OpenCV.

Hand Detection: MediaPipe identifies hand landmarks.

Distance Calculation: Calculates distance between thumb tip (landmark 4) and index tip (landmark 8).

Volume Mapping: Maps the distance to system volume using PyCaw.

Visualization: Displays a real-time volume bar and the numeric volume percentage.

# Notes

Only works on Windows due to PyCaw dependency.

Adjust the smoothness variable in the code to change the volume smoothing factor.

Ensure good lighting for reliable hand detection.

License
MIT License © [AADITYA]
