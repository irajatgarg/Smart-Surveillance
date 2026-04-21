# modules/output.py

import cv2
from config import WINDOW_NAME

class OutputHandler:

    @staticmethod
    def display(frame, text):
        cv2.putText(frame, text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv2.imshow(WINDOW_NAME, frame)