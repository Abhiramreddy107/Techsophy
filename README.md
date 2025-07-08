# 🚗 Telematics-Based Usage Insurance System

This project simulates a **Usage-Based Insurance (UBI)** system that adjusts insurance premiums based on **real-time driving behavior**. It uses **AI/ML** to classify behavior, calculate risk scores, adjust premiums, and provide personalized feedback — all through **continuous telematics data streaming**.

---

## 🎯 Key Features

- ✅ Real-time telematics data simulation (speed, acceleration, braking)
- ✅ ML-based driving behavior classification (`safe`, `moderate`, `risky`)
- ✅ Risk score computation (0–100)
- ✅ Usage-based premium adjustment (discount/penalty)
- ✅ Personalized feedback for safety improvement
- ✅ Modular structure (data, model, scoring, pricing, feedback)
- ✅ Stream-ready architecture (evaluates every 10 seconds)

---

## 🧠 Technologies Used

- Python 3.10+
- scikit-learn (for ML)
- NumPy (for feature extraction)
- Time-based simulation (no real sensors yet)

---

## 📁 Project Structure

```
telematics_insurance/
├── main.py                     # Main execution script (streaming logic)
├── stream_generator.py         # Real-time data simulator (1 datapoint/sec)
├── behavior_model.py           # ML model for behavior classification
├── risk_scoring.py             # Maps behavior to risk score
├── premium_adjustment.py       # Adjusts insurance premium based on risk
├── feedback_system.py          # Provides user feedback
├── utils.py                    # Generates mock training data
└── README.md                   # Project documentation
```

---

## 🚀 How to Run

1. **Install dependencies** (once):
```bash
pip install scikit-learn numpy
```

2. **Run the system**:
```bash
python main.py
```

3. Output appears every second, with a full driving evaluation every 10 seconds:
```
📊 Evaluation at 10 seconds
Behavior: moderate
Risk Score: 50
Adjusted Premium: ₹5000
Feedback: Drive more cautiously, especially in traffic
```

---

## 📊 Sample Output :

```
Received: {'speed': 78, 'acceleration': 1.5, 'braking': 0.2, 'timestamp': 9}
📊 Evaluation at 10 seconds
Behavior: safe
Risk Score: 20
Adjusted Premium: ₹4500
Feedback: Great driving! Keep it up!
```

---

## 📦 Deliverables

| Module | Description |
|--------|-------------|
| Data Streaming | Simulates telematics stream (1 datapoint/sec) |
| Behavior Model | Classifies driving style using RandomForest |
| Risk Engine | Calculates risk score from behavior |
| Premium Engine | Adjusts insurance cost dynamically |
| Feedback | Gives user actionable advice |
| Stream Pipeline | Repeats every 10 seconds with real-time output |

---


