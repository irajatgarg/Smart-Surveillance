# modules/video_input.py

import cv2

class VideoInput:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)

    def get_frame(self):
        ret, frame = self.cap.read()
        return ret, frame

    def release(self):
        self.cap.release()