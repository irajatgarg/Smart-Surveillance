# modules/feature_extraction.py

import cv2
import numpy as np
from config import MIN_CONTOUR_AREA

class FeatureExtractor:

    @staticmethod
    def extract(prev_frame, curr_frame):
        if prev_frame is None:
            return [], curr_frame

        diff = cv2.absdiff(prev_frame, curr_frame)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        objects = []
        for cnt in contours:
            if cv2.contourArea(cnt) > MIN_CONTOUR_AREA:
                objects.append(cnt)

        return objects, curr_frame