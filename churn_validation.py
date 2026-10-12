REQUIRED_FEATURES = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "InternetService",
    "Contract",
    "MonthlyCharges",
    "TotalCharges",
]


def validate_churn_input(data):
    for feature in REQUIRED_FEATURES:
        if feature not in data:
            return False

        if data[feature] is None:
            return False

    try:
        if float(data["SeniorCitizen"]) not in (0, 1):
            return False

        if float(data["tenure"]) < 0:
            return False

        if float(data["MonthlyCharges"]) < 0:
            return False

        if float(data["TotalCharges"]) < 0:
            return False

    except (ValueError, TypeError):
        return False

    return True
