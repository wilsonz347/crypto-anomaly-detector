"""Use the loaded model/scaler directly for predictions."""

import bentoml
from bentoml.io import JSON
import pandas as pd 
import numpy as np

scaler = bentoml.sklearn.load_model("scaler:latest")
model = bentoml.sklearn.get("anomaly_model:latest").to_runner()
service = bentoml.Service("crypto_anomaly_detection", runners=[model])

# Feature columns
FEATURE_COLUMNS = [
  "High_log", "Low_log", "Open_log", "Close_log", 
  "Volume_log", "Marketcap_log", 
  "log_return", "log_high_low_spread", "log_close_open_return"
]

# Initialize API & make prediction
@service.api(input=JSON(), output=JSON()) 
async def predict(input_data):
  try:
    df = pd.DataFrame([input_data])
    df = df.dropna().drop_duplicates()
    
    # Apply logarithmic transformation to target columns
    """Original log transformed columns"""
    cols = ['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']
    epsilon = 1e-9  # to avoid log(0)
    for col in cols:
        df[f"{col}_log"] = np.log(df[col] + epsilon)
        
    # Compute necessary features
    df['log_return'] = df['Close_log'] - df['Open_log']
    df['log_high_low_spread'] = df['High_log'] - df['Low_log']
    df['log_close_open_return'] = df['Close_log'] - df['Open_log']
    
    features = df[FEATURE_COLUMNS]
    
    # Scale & make prediction
    scaled_features = scaler.transform(features)
    
    prediction = await model.async_run(scaled_features)
    
    # Map prediction (-1: anomaly, 1: normal) to boolean
    anomaly_flags = [bool(p == -1) for p in prediction]
    
    return {"anomaly": anomaly_flags[0]}
  
  except Exception as e:
    return {"error": str(e)}