# modules/preprocessing.py

import cv2
from config import FRAME_WIDTH, FRAME_HEIGHT

class Preprocessing:

    @staticmethod
    def process(frame):
        resized = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        return resized, blur