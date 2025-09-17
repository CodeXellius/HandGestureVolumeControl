import cv2
import mediapipe as mp
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# -------------------- Setup --------------------
# Webcam capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

# MediaPipe hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# PyCaw volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_min, vol_max = volume.GetVolumeRange()[:2]

# Smoothing factor
smoothness = 5

print(f"Volume range: {vol_min} to {vol_max}")

# -------------------- Main Loop --------------------
while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # Get landmark positions
            lmList = []
            h, w, c = img.shape
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            if lmList:
                # Thumb tip (id=4) and Index tip (id=8)
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]

                # Draw circles and connecting line
                cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

                # Distance between thumb and index
                length = np.hypot(x2 - x1, y2 - y1)

                # Map distance to volume
                vol = np.interp(length, [30, 200], [vol_min, vol_max])
                # Smooth volume
                vol_bar = int(np.interp(length, [30, 200], [0, 100]))
                vol_bar = round(vol_bar / smoothness) * smoothness
                volume.SetMasterVolumeLevel(np.interp(vol_bar, [0, 100], [vol_min, vol_max]), None)

                # Volume bar visualization
                bar = np.interp(length, [30, 200], [400, 150])
                cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 0), 3)
                cv2.rectangle(img, (50, int(bar)), (85, 400), (0, 255, 0), cv2.FILLED)

                # Display distance & volume percentage
                cv2.putText(img, f'Distance: {int(length)}', (400, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                cv2.putText(img, f'Volume: {int(np.interp(length, [30, 200], [0, 100]))}%', (400, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Debug in console
                # print(f"Length: {length:.2f} | Volume: {vol:.2f}")

    # Show webcam feed
    cv2.imshow("Hand Volume Control", img)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------- Cleanup --------------------
cap.release()
cv2.destroyAllWindows()
