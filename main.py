from stream_generator import telematics_stream
from behavior_model import DrivingBehaviorModel
from risk_scoring import calculate_risk_score
from premium_adjustment import adjust_premium
from feedback_system import generate_feedback
from utils import create_mock_training_data

def main():
    print("🚗 Starting Continuous Telematics Stream...")

    # 1. Train model
    model = DrivingBehaviorModel()
    X_train, y_train = create_mock_training_data()
    model.train(X_train, y_train)

    # 2. Prepare sliding window
    window = {"speed": [], "acceleration": [], "braking": [], "timestamp": []}
    base_premium = 5000

    # 3. Loop through real-time simulated stream
    for datapoint in telematics_stream("trip-123", duration=60):
        print(f"Received: {datapoint}")
        for key in window:
            window[key].append(datapoint[key])

        # 4. Keep only latest 10 data points
        if len(window["speed"]) > 10:
            for key in window:
                window[key].pop(0)

        # 5. Evaluate behavior every 10 seconds
        if datapoint["timestamp"] % 10 == 9:
            features = model.extract_features(window)
            behavior = model.predict(features)
            risk_score = calculate_risk_score(behavior)
            adjusted_premium = adjust_premium(base_premium, risk_score)
            feedback = generate_feedback(behavior)

            print(f"\n📊 Evaluation at {datapoint['timestamp'] + 1} seconds")
            print("Behavior:", behavior)
            print("Risk Score:", risk_score)
            print("Adjusted Premium: ₹", round(adjusted_premium))
            print("Feedback:", feedback)
            print("-" * 40)

if __name__ == "__main__":
    main()
