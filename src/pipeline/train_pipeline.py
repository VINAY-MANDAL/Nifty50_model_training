import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.components.data_transformation import transform_data
from src.components.model_trainer import train_random_forest

def run_pipeline():
    print("🚀 Starting ML Training Pipeline...")

    raw_data_path = "data_set/row/Nifty_50_India_2000_2026.csv"

    if not os.path.exists(raw_data_path):
        raw_data_path = "../data_set/row/Nifty_50_India_2000_2026.csv"

    print("⏳ Transforming data and engineering features...")
    df_cleaned = transform_data(raw_data_path)
    print(f"✔ Data transormed! Shape: {df_cleaned.shape} ")

    print("⏳ Training Random Forest Classifier...")
    model, accuracy = train_random_forest(df_cleaned)

    print('\n==================================')
    print(f"📈 Random Forest Test Accuracy: {accuracy:.4f}")
    print("=======================================")

if __name__ == "__main__":
    run_pipeline()