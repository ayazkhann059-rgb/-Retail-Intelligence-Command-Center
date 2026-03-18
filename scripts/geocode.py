import pandas as pd

df = pd.read_csv("data/final_data.csv")

coords = {
    "Delhi": (28.61, 77.23),
    "Mumbai": (19.07, 72.87),
    "Pune": (18.52, 73.85),
    "Kolkata": (22.57, 88.36),
    "Bangalore": (12.97, 77.59)
}

df["lat"] = df["city"].apply(lambda x: coords[x][0])
df["lng"] = df["city"].apply(lambda x: coords[x][1])

df.to_csv("data/final_data.csv", index=False)

print("✅ Geocoding added!")
