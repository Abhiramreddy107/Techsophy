import random

def create_mock_training_data():
    X, y = [], []
    for _ in range(300):
        speed = random.uniform(40, 80)
        std_speed = random.uniform(5, 25)
        acc = random.uniform(0.5, 3.5)
        brake = random.uniform(0.1, 1.0)

        if acc < 1.0 and brake < 0.3:
            label = "safe"
        elif acc < 2.0:
            label = "moderate"
        else:
            label = "risky"

        X.append([speed, std_speed, acc, brake])
        y.append(label)
    return X, y
