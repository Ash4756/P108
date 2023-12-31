import cv2
import mediapipe as mp 
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)
def drawhandlandmarks(image,hand_landmarks):
    if hand_landmarks :
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(image,landmarks,mp_hands.HAND_CONNECTIONS)
while True:
    success, image = cap.read()
    image = cv2.flip(image,1)
    result = hands.process(image)
    hand_landmarks = result.multi_hand_landmarks
    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

