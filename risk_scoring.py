def calculate_risk_score(behavior_label):
    score_map = {
        "safe": 20,
        "moderate": 50,
        "risky": 90
    }
    return score_map.get(behavior_label, 60)
