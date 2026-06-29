import pandas as pd
import numpy as np

def transform_data(raw_data_path):
    # 1. Load original data
    df = pd.read_csv(raw_data_path)
    
    # 2. Clean structure
    df_clean = df.drop([0, 1]).reset_index(drop=True)
    df_clean.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
    
    # 3. Convert types
    numeric_cols = ['Close', 'High', 'Low', 'Open', 'Volume']
    for col in numeric_cols:
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    df_clean['Date'] = pd.to_datetime(df_clean['Date'], errors='coerce')
    df_clean.dropna(inplace=True)
    
    # 4. Target Variable
    df_clean['Next_Close'] = df_clean['Close'].shift(-1)
    df_clean['Target'] = (df_clean['Next_Close'] > df_clean['Close']).astype(int)
    
    # 5. Feature Engineering
    df_clean['Return'] = df_clean['Close'].pct_change()
    df_clean['MA_5'] = df_clean['Close'].rolling(window=5).mean()
    df_clean['Ratio_MA_5'] = df_clean['Close'] / df_clean['MA_5']
    df_clean['Volatility_5'] = df_clean['Return'].rolling(window=5).std()
    
    df_clean.dropna(inplace=True)
    return df_clean