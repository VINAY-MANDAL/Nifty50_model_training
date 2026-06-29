import sys
import os
import joblib
import pandas as pd

# 'src' folder ko import karne ke liye path append
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class PredictPipeline:
    def __init__(self):
        self.model_path = os.path.join('models', 'nifty50_rf_model.pkl')
        if not os.path.exists(self.model_path):
            self.model_path = os.path.join('../../models', 'nifty50_rf_model.pkl')

    def predict(self, features_dict):
        """
        features_dict: {'Return': 0.015, 'Ratio_MA_5': 1.02, 'Volatility_5': 0.008}
        """
        if not os.path.exists(self.model_path):
            return "❌ Error: Trained model file (.pkl) nahi mili! Pehle train_pipeline.py chalayein."
        
        # Model ko load karna
        model = joblib.load(self.model_path)
        
        # Input data ko DataFrame me badalna
        input_df = pd.DataFrame([features_dict])
        
        # Prediction nikalna
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][prediction]
        
        return prediction, probability

if __name__ == "__main__":
    # Test karne ke liye ek dummy data dete hain (Maan lo aaj market 1.2% return diya)
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