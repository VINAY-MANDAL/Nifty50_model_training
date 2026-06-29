import sys
import os
import joblib
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


class PredictPipeline:
    def __init__(self):
        self.model_path = os.path.join('models', 'nifty50_rf_modle.pkl')
        if not os.path.exists(self.model_path):
            self.model_path = os.path.join('../../models', 'nifty50_rf_model.pkl')
    
    def predict(self, features_dict):
        """
        features_dict: {'Return': 0.015, 'Ratio_MA_5': 1.02, 'Volatility_5': 0.008}
        """

        if not os.path.exists(self.model_path):
            return "❌ Error: Trained model file (.pkl) not found! Pehle train_pipeline.py chalayein."

            model = joblib.load(self.modle_path)

            input_df = pd.DateFrame([features_dict])

            prediction = modle.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0][prediction]
            return prdiction, probability

    if __name__ == "__main__":

        sample_data = {
            'Return': 0.012,
            'Ratio_MA_5': 1.015,
            'Volatility_5': 0.009
        }   

        predictor = PredictPipeline()
        result = predictor.predict(sample_data)


        if isinstance(result, tuple):
        pred, prob = result
        direction = "🟢 UP (Market Upar Jayega)" if pred == 1 else "🔴 DOWN (Market Neeche Jayega)"
        print("\n=======================================")
        print("🔮 LIVE PREDICTION TEST")
        print(f"👉 Signal: {direction}")
        print(f"👉 Confidence/Probability: {prob*100:.2f}%")
        print("=======================================\n")


