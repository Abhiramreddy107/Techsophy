def adjust_premium(base_premium, risk_score):
    if risk_score < 30:
        return base_premium * 0.9  # 10% discount
    elif risk_score < 70:
        return base_premium
    else:
        return base_premium * 1.2  # 20% increase
