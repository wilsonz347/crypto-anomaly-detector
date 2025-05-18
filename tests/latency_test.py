import requests
import time

data = {
    "High": 67000,
    "Low": 66000,
    "Open": 66500,
    "Close": 66800,
    "Volume": 3400000000,
    "Marketcap": 1300000000000
}

# Measure latency
start = time.time()
response = requests.post("http://localhost:3000/predict", json=data)
end = time.time()

print("Response JSON:", response.json())
print("Latency (ms):", round((end - start) * 1000, 2))