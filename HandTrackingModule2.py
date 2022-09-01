import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode = false, maxHands = 2, detectionCon = 0.5, trackCon = 0.5)