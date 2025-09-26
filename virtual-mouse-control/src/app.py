# Fix OpenCV-PyAutoGUI compatibility issue
import sys
import cv2

# Ensure cv2 has __version__ attribute before importing pyautogui
if not hasattr(cv2, '__version__'):
    cv2.__version__ = '4.8.0'

# Now safely import other modules
import mediapipe as mp
import pyautogui
import time
import math

# Configure PyAutoGUI
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Screen size
screen_width, screen_height = pyautogui.size()

# Webcam
cap = cv2.VideoCapture(0)

# Drag state
dragging = False

def get_distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    h, w, _ = img.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Fingertip landmarks
            index_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            middle_tip = hand_landmarks.landmark[12]
            ring_tip = hand_landmarks.landmark[16]

            # Screen coordinates
            screen_x = int(index_tip.x * screen_width)
            screen_y = int(index_tip.y * screen_height)

            # Move mouse
            pyautogui.moveTo(screen_x, screen_y)

            # Draw fingertip
            x, y = int(index_tip.x * w), int(index_tip.y * h)
            cv2.circle(img, (x, y), 10, (255, 0, 255), cv2.FILLED)

            # Gesture: Click (pinch index + thumb)
            pinch_distance = get_distance(index_tip, thumb_tip)
            if pinch_distance < 0.03:
                pyautogui.click()
                cv2.putText(img, "Click", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                time.sleep(0.2)

            # Gesture: Scroll (middle finger up/down)
            middle_y = int(middle_tip.y * h)
            if middle_y < y - 40:
                pyautogui.scroll(20)
                cv2.putText(img, "Scroll Up", (x, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            elif middle_y > y + 40:
                pyautogui.scroll(-20)
                cv2.putText(img, "Scroll Down", (x, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            # Gesture: Drag (pinch and hold)
            if pinch_distance < 0.03 and not dragging:
                pyautogui.mouseDown()
                dragging = True
                cv2.putText(img, "Drag Start", (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            elif pinch_distance > 0.05 and dragging:
                pyautogui.mouseUp()
                dragging = False
                cv2.putText(img, "Drag End", (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

            # Gesture: App switch (three fingers close together)
            dist_ring = get_distance(index_tip, ring_tip)
            dist_middle = get_distance(index_tip, middle_tip)
            if dist_ring < 0.03 and dist_middle < 0.03:
                pyautogui.hotkey('alt', 'tab')
                cv2.putText(img, "Switch App", (x, y + 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                time.sleep(0.5)

    cv2.imshow("Gesture-Controlled Interface", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()