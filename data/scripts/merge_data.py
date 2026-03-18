import pandas as pd

mock = pd.read_csv("data/mockaroo_data.csv")

# Add simulated competitor prices
mock["competitor_price"] = [55, 50, 28, 30, 115]

mock.to_csv("data/final_data.csv", index=False)

print("✅ Data merged!")
