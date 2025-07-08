from sklearn.ensemble import RandomForestClassifier
import numpy as np

class DrivingBehaviorModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.trained = False

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        self.trained = True

    def predict(self, features):
        if not self.trained:
            raise ValueError("Model not trained.")
        return self.model.predict([features])[0]

    def extract_features(self, data):
        return [
            np.mean(data["speed"]),
            np.std(data["speed"]),
            max(data["acceleration"]),
            max(data["braking"])
        ]
