from sklearn.ensemble import RandomForestClassifier
import json

def train_random_forest(df):
    # Split
    split_index = int(len(df) * 0.8)
    features = ['Return', 'Ratio_MA_5', 'Volatility_5']
    
    X_train = df[features].iloc[:split_index]
    y_train = df['Target'].iloc[:split_index]
    X_test = df[features].iloc[split_index:]
    y_test = df['Target'].iloc[split_index:]
    
    # Train
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    accuracy = model.score(X_test, y_test)
    return model, accuracy