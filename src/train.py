"""
This script performs anomaly detection on cryptocurrency data using Isolation Forest.
It preprocesses log-transformed features, normalizes them with StandardScaler,
trains the Isolation Forest model, predicts anomalies, calculates anomaly scores,
and saves the scaler and model for future use.
"""

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import joblib

data = pd.read_csv("../data/processed_crypto_data.csv")

features = [
  "High_log", "Low_log", "Open_log", "Close_log", 
  "Volume_log", "Marketcap_log", 
  "log_return", "log_high_low_spread", "log_close_open_return"
]
features = data[features]

# Initialize the scaler
scaler = StandardScaler() # Helps with normalizing the logarithmic transformed data
feature_scaled = scaler.fit_transform(features)

# Train the model (with 1% expected contamination)
iso_forest = IsolationForest(contamination=0.01, random_state=100)
iso_forest.fit(feature_scaled)

# Prediction (-1: Anomaly, 1: Normal)
data['isolation_anomaly'] = iso_forest.predict(feature_scaled)
data['isolation_anomaly'] = data['isolation_anomaly'].map({1: False, -1: True})

# Evaluate using decision_function() -> compute an anomaly score (lower scores indicate more anomalous points)
scores = iso_forest.decision_function(feature_scaled)
data['anomaly_score'] = scores
print(data['isolation_anomaly'].value_counts()) # Generalization of all anomalies

# Visualization
plt.hist(data['anomaly_score'], bins=50)
plt.title('Distribution of Anomaly Scores')
plt.xlabel('Anomaly Score')
plt.ylabel('Frequency')
plt.show()

"""
The histogram above is skewed to the left, indicating that majority of the points
have higher anomaly scores (look more normal).
"""

# Save the scaler & model
joblib.dump(scaler, '../models/scaler.pkl')
joblib.dump(iso_forest, '../models/anomaly_detection.pkl')