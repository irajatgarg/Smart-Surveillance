# main.py

import cv2
from modules.yolo_detector import YOLODetector
import winsound
import time
from modules.video_input import VideoInput
from modules.preprocessing import Preprocessing
from modules.feature_extraction import FeatureExtractor
from modules.analysis import AnalysisEngine
from modules.interpretation import InterpretationEngine
from modules.output import OutputHandler

def main():
    video = VideoInput(0)
    detector = YOLODetector()
    last_alert_time = 0
    prev_frame = None

    while True:
        ret, frame = video.get_frame()

        if not ret:
            break

        boxes = detector.detect(frame)
        person_detected = len(boxes) > 0

        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        processed_frame, gray = Preprocessing.process(frame)
        objects, prev_frame = FeatureExtractor.extract(prev_frame, gray)
        state, count = AnalysisEngine.analyze(objects)
        explanation = InterpretationEngine.interpret(state, count)

        if person_detected:
            explanation = "🚨 Person Detected!"
            if time.time() - last_alert_time > 3:
                winsound.Beep(1000, 500)
                last_alert_time = time.time()
                cv2.imwrite(f"snap_{int(time.time())}.jpg", frame)

        OutputHandler.display(frame, explanation)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()   
