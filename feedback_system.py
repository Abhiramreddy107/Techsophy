def generate_feedback(behavior_label):
    if behavior_label == "safe":
        return "Great driving! Keep it up!"
    elif behavior_label == "moderate":
        return "Drive a bit more cautiously, especially in high-traffic areas."
    elif behavior_label == "risky":
        return "High risk detected! Avoid harsh braking and rapid acceleration."
    return "Data insufficient to evaluate feedback."
