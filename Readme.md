📊 Stock Market Trend Prediction using Machine Learning

A machine learning project that predicts stock market trends using engineered technical indicators and ensemble learning techniques. The project follows a modular pipeline architecture for data preprocessing, feature engineering, model training, and inference.

---

🛠️ Key Technical Features

🔹 Automated Structural Data Cleaning

- Removes raw layout noise and structural irregularities.
- Handles data-type coercions using programmatic Pandas routines.
- Produces a clean and consistent dataset for model training.

🔹 Time-Series Feature Engineering

Engineers meaningful market indicators instead of relying solely on raw price values.

Features include:

- Daily Percentage Returns – Captures short-term market momentum.
- 5-Day Moving Average Ratio – Measures price deviation from recent trends.
- 5-Day Rolling Volatility – Models short-term market risk and uncertainty.

🔹 Sequential Data Splitting

- Prevents data leakage by maintaining chronological order.
- 80% historical data for training.
- 20% future data for testing.

🔹 Ensemble Model Optimization

- Upgrades from baseline models to a Random Forest Classifier.
- Reduces prediction variance through ensemble voting.
- Improves generalization on unseen market data.

---

🚀 Getting Started

1️⃣ Installation

Clone the repository and install the required dependencies.

pip install -r requirements.txt

---

2️⃣ Train the Model

Run the complete training pipeline to:

- Load the dataset
- Clean and preprocess data
- Generate technical indicators
- Train the Random Forest model
- Save the trained model

python src/pipeline/train_pipeline.py

---

3️⃣ Run Predictions

Generate predictions using the trained model without retraining.

python src/pipeline/predict_pipeline.py

---

📈 Performance Results

Model| Performance
Logistic Regression| ~53% Accuracy (High bias; frequently predicted UP movements)
Decision Tree (Max Depth = 3)| Improved class balance using engineered features
Random Forest Classifier| 54% – 62% Test Accuracy through ensemble learning

---

🧰 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Git
- Modular Machine Learning Pipeline

---

👨‍💻 Developer

Vinay Kumar Mandal

Role: Software Developer & Machine Learning Engineer

Core Skills

- Machine Learning
- Python
- Scikit-Learn
- Pandas
- Git
- Modular Pipeline Design

---

📚 Notes

This project was developed as a practical implementation of Ensemble Learning (Chapters 6 & 7), focusing on Random Forest architectures, feature engineering, and production-oriented machine learning pipeline design.