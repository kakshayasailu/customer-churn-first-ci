import unittest
from churn_validation import validate_churn_input


class TestChurnValidation(unittest.TestCase):

    def setUp(self):
        self.valid_data = {
            "gender": "Female",
            "SeniorCitizen": 0,
            "Partner": "Yes",
            "Dependents": "No",
            "tenure": 12,
            "PhoneService": "Yes",
            "InternetService": "DSL",
            "Contract": "Month-to-month",
            "MonthlyCharges": 70.35,
            "TotalCharges": 844.2
        }

    def test_valid_churn_input(self):
        self.assertTrue(validate_churn_input(self.valid_data))

    def test_missing_feature(self):
        data = self.valid_data.copy()
        del data["tenure"]
        self.assertFalse(validate_churn_input(data))

    def test_negative_value(self):
        data = self.valid_data.copy()
        data["MonthlyCharges"] = -10
        self.assertFalse(validate_churn_input(data))

    def test_non_numeric_value(self):
        data = self.valid_data.copy()
        data["tenure"] = "hello"
        self.assertFalse(validate_churn_input(data))


if __name__ == "__main__":
    unittest.main()
