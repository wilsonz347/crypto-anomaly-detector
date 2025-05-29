import requests
import pandas as pd
from tqdm import tqdm

input_path = "../data/synthetic_data.csv" 
output_path = "../data/anomaly_predictions.csv"

df = pd.read_csv(input_path)

results = []

for _, row in tqdm(df.iterrows(), total=len(df), desc="Generating Predictions..."):
    try:
        input_payload = {
            "High": row["High"],
            "Low": row["Low"],
            "Open": row["Open"],
            "Close": row["Close"],
            "Volume": row["Volume"],
            "Marketcap": row["Marketcap"]
        }
        
        # Send post request to API endpoint
        response = requests.post("http://localhost:3000/predict", json=input_payload)
        result_json = response.json()
        
        result = input_payload.copy()
        result["anomaly"] = result_json.get("anomaly", None)
        results.append(result)
    
    except Exception as e:
        print(f"Error: {e}")
    
# Save to output csv
results_df = pd.DataFrame(results)
results_df.to_csv(output_path, index=False)
print(f"✅ Anomaly predictions saved to: {output_path}")