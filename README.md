
# 🧠 AI-Enabled Smart Surveillance System (Lightweight & Legacy-Compatible)

A modular, lightweight surveillance system designed to simulate an AI-powered video analysis pipeline while being fully compatible with low-resource local machines.

This project follows a **hybrid intelligent pipeline architecture** inspired by modern AI/ML surveillance systems, but optimized for **real-time execution without heavy dependencies or GPU requirements**.

---

## 📌 Key Features

- 🎥 Real-time video processing (webcam / video input)
- ⚙️ Modular pipeline architecture (industry-style design)
- 🧩 Motion-based feature extraction (lightweight alternative to deep learning)
- 📊 Activity classification (Normal / High / No activity)
- ⚠️ Risk scoring mechanism
- 📝 Event logging system
- 📸 Automatic anomaly snapshot capture
- 🧠 Explainable output (human-readable interpretations)

---

## 🏗️ System Architecture

The system follows a **layered modular pipeline**, similar to enterprise AI surveillance systems:

```

Video Input → Preprocessing → Feature Extraction → Analysis Engine → Interpretation Layer → Output Module

```

### 🔹 Module Breakdown

1. **Video Input Module**
   - Captures video stream from webcam or file
   - Handles frame acquisition

2. **Preprocessing Module**
   - Resizes frames
   - Converts to grayscale
   - Applies noise reduction (Gaussian blur)

3. **Feature Extraction Module**
   - Uses frame differencing
   - Detects motion regions (contours)
   - Acts as lightweight “object detection”

4. **Analysis Engine**
   - Counts detected motion regions
   - Classifies activity:
     - No Activity
     - Normal Activity
     - High Activity (Anomaly)

5. **Interpretation Layer**
   - Converts system output into human-readable explanations
   - Simulates explainable AI behavior

6. **Output Module**
   - Displays live annotated video
   - Shows activity status + risk score

7. **Utility Layer**
   - Risk score calculation
   - Logging system
   - Snapshot capture

---

## ⚙️ How It Works

1. Video frames are captured in real-time  
2. Frames are preprocessed to normalize input  
3. Motion is detected using frame differencing  
4. Significant moving regions are extracted  
5. Activity level is classified based on movement intensity  
6. A **risk score** is calculated  
7. The system generates:
   - Real-time alerts
   - Logs
   - Snapshots (for anomalies)

---

## 📁 Project Structure

```

smart_surveillance/
│
├── main.py
├── config.py
├── requirements.txt
│
├── modules/
│   ├── video_input.py
│   ├── preprocessing.py
│   ├── feature_extraction.py
│   ├── analysis.py
│   ├── interpretation.py
│   ├── output.py
│
├── utils/
│   └── helpers.py
│
├── logs.txt (auto-generated)
├── snapshots/ (auto-created)
└── README.md

```

---

## 🚀 Setup & Run Instructions

### 1️⃣ Clone the repository

```

git clone [https://github.com/YOUR-USERNAME/smart-surveillance-system.git](https://github.com/YOUR-USERNAME/smart-surveillance-system.git)
cd smart-surveillance-system

```

---

### 2️⃣ (Optional) Create virtual environment

```

python -m venv .venv
.venv\Scripts\activate   # Windows

```


#️⃣ Install dependencies
pip install -r requirements.txt



```


4️⃣ Run the system
python main.py



```

---

## 🎯 Output

The system displays a live video feed with intelligent annotations:

Examples:

- `No significant activity`
- `Normal movement detected (2 objects)`
- `⚠ High movement detected (7 objects) | Risk: 90%`

---

## 📊 Generated Outputs

### 📝 logs.txt
Tracks system activity over time:
```

[2026-04-21 12:01:10] NORMAL_ACTIVITY - 2 objects
[2026-04-21 12:01:15] HIGH_ACTIVITY - 7 objects

```

### 📸 snapshots/
- Stores images when anomalies are detected

---

## 💡 Design Philosophy

This system is built to demonstrate:

- **Hardware-agnostic intelligence layer**
- **Lightweight AI-inspired pipeline**
- **Edge-compatible surveillance processing**
- **Explainable system outputs**

It avoids heavy ML models while maintaining the **structure and behavior of intelligent surveillance systems**.

---

## ⚠️ Limitations

- Does not use deep learning models (by design for lightweight execution)
- Motion-based detection may be sensitive to lighting changes
- Not suitable for high-security production environments

---

## 🔮 Future Enhancements

- Integration with real object detection models (YOLO, etc.)
- Web dashboard for monitoring
- Cloud-based logging & analytics
- Multi-camera support

---

## 👨‍💻 Author

**Rachit Garg**

---

## 📄 License

This project is for educational and demonstration purposes.
