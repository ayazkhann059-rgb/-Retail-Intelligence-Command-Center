import pandas as pd
from scipy.stats import zscore

df = pd.read_csv("data/final_data.csv")

df["z_score"] = zscore(df["price"])
df["anomaly"] = df["z_score"].apply(lambda x: "Yes" if abs(x) > 2 else "No")

df.to_csv("data/final_data.csv", index=False)

print("✅ Anomaly detection complete!")
