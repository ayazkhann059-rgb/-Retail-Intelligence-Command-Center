import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/category/books_1/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = []

for item in soup.find_all("article", class_="product_pod"):
    name = item.h3.a["title"]
    price = item.find("p", class_="price_color").text

    products.append({
        "raw_text": f"{name} costs {price}"
    })

df = pd.DataFrame(products)
df.to_csv("data/scraped_data.csv", index=False)

print("✅ Scraped data saved!")
