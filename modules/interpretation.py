# modules/interpretation.py

class InterpretationEngine:

    @staticmethod
    def interpret(state, count):
        if state == "HIGH_ACTIVITY":
            return f"⚠ High movement detected ({count} objects) - Possible anomaly"
        elif state == "NORMAL_ACTIVITY":
            return f"Normal movement detected ({count} objects)"
        else:
            return "No significant activity"