import pandas as pd
import openai

openai.api_key = "YOUR_API_KEY"

df = pd.read_csv("data/scraped_data.csv")

cleaned_rows = []

for text in df["raw_text"]:
    prompt = f"""
    Extract:
    product_name, category, brand, price

    from this text:
    {text}

    Return JSON.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    cleaned_rows.append(response['choices'][0]['message']['content'])

clean_df = pd.DataFrame({"cleaned_data": cleaned_rows})
clean_df.to_csv("data/cleaned_data.csv", index=False)

print("✅ Cleaned data saved!")
