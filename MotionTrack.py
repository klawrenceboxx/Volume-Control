#framework we are going to use is mediapipe

import cv2 
import mediapipe as mp
import time

#The basic code needed to code any webcam
#__________________________
cap = cv2.VideoCapture()

while True:
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitkey(1)
#__________________________