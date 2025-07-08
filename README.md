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
- ✅ **Privacy-aware** system with trip anonymization
- ✅ **Consent control** before monitoring starts

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
├── main.py                     # Main execution script (streaming logic + privacy)
├── stream_generator.py         # Real-time data simulator (1 datapoint/sec, UUID trip ID)
├── behavior_model.py           # ML model for behavior classification
├── risk_scoring.py             # Maps behavior to risk score
├── premium_adjustment.py       # Adjusts insurance premium based on risk
├── feedback_system.py          # Provides user feedback
├── utils.py                    # Generates mock training data
└── README.md                   # Project documentation
```

---

## 🚀 How to Run

1. **Install dependencies**:
```bash
pip install scikit-learn numpy
```

2. **Run the system**:
```bash
python main.py
```

3. ✅ Output appears every second, with a full driving evaluation every 10 seconds:
```
📊 Evaluation at 10 seconds
Trip ID: d47f38c2-43a4-420f-b9fc-fadf4126d3be
Behavior: moderate
Risk Score: 50
Adjusted Premium: ₹5000
Feedback: Drive more cautiously, especially in traffic
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
| Privacy Layer | Anonymizes trip ID using UUID |
| Consent Gate | Allows simulation of opt-in tracking |

---


