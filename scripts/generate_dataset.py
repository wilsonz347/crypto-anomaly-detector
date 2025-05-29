import pandas as pd
import numpy as np

np.random.seed(42)

num_rows = 1000

# Generate synthetic values
high = np.random.normal(loc=30000, scale=5000, size=num_rows)
low = high - np.random.uniform(200, 2000, size=num_rows)
open_ = low + np.random.uniform(100, 1000, size=num_rows)
close = open_ + np.random.uniform(-1500, 1500, size=num_rows)
volume = np.random.uniform(1e8, 1e10, size=num_rows)
marketcap = np.random.uniform(1e11, 2e12, size=num_rows)

df = pd.DataFrame({
    "High": np.round(high, 2),
    "Low": np.round(low, 2),
    "Open": np.round(open_, 2),
    "Close": np.round(close, 2),
    "Volume": np.round(volume, 2),
    "Marketcap": np.round(marketcap, 2)
})

output_path = "../data/synthetic_data.csv"
df.to_csv(output_path, index=False)