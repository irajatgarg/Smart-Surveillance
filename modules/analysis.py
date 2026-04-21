# modules/analysis.py

from config import MOTION_THRESHOLD

class AnalysisEngine:

    @staticmethod
    def analyze(objects):
        count = len(objects)

        if count > 5:
            return "HIGH_ACTIVITY", count
        elif count > 0:
            return "NORMAL_ACTIVITY", count
        else:
            return "NO_ACTIVITY", count