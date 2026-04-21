# utils/helpers.py

import datetime
import os


# 🕒 Get current timestamp
def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ⚠ Risk score calculation (simple but looks AI-driven)
def calculate_risk(count):
    if count == 0:
        return 0
    elif count <= 3:
        return 30
    elif count <= 6:
        return 60
    else:
        return 90


# 📝 Log events to file
def log_event(state, count):
    timestamp = get_timestamp()
    log_line = f"[{timestamp}] {state} - {count} objects\n"

    with open("logs.txt", "a") as file:
        file.write(log_line)


# 📸 Save anomaly snapshot
def save_snapshot(frame):
    if not os.path.exists("snapshots"):
        os.makedirs("snapshots")

    filename = datetime.datetime.now().strftime("snapshots/anomaly_%H%M%S.jpg")
    import cv2
    cv2.imwrite(filename, frame)