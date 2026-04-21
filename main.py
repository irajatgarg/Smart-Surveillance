# main.py

import cv2
from modules.video_input import VideoInput
from modules.preprocessing import Preprocessing
from modules.feature_extraction import FeatureExtractor
from modules.analysis import AnalysisEngine
from modules.interpretation import InterpretationEngine
from modules.output import OutputHandler

def main():
    video = VideoInput(0)
    prev_frame = None

    while True:
        ret, frame = video.get_frame()
        if not ret:
            break

        processed_frame, gray = Preprocessing.process(frame)

        objects, prev_frame = FeatureExtractor.extract(prev_frame, gray)

        state, count = AnalysisEngine.analyze(objects)

        explanation = InterpretationEngine.interpret(state, count)

        OutputHandler.display(processed_frame, explanation)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()