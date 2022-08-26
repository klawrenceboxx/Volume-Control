#framework we are going to use is mediapipe

import cv2 
import mediapipe as mp
import time

#The basic code needed to code any webcam
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#initilizing previous and current time to zero
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    #mpHands.Hand_CONNECTIONS draws the lines between the points
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 4:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #converts the time into a string, makes it an integer, gives it a value and position
    #cv2.FONT gives our font, '3' is the scale, next is the color (purple), & thickness (3)
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, 
    (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

# code to let us escape the webcam
    if key == 27:
        break

#github hosts our shit


#make comments after 19:00