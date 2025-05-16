import joblib
import bentoml

# Load existing pkl models
scaler = joblib.load('../models/scaler.pkl')
anomaly_model = joblib.load('../models/anomaly_detection.pkl')

# Save to BentoML model store
bentoml.sklearn.save_model('scaler', scaler)
bentoml.sklearn.save_model('anomaly_model', anomaly_model)