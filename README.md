# Retail Intelligence Command Center

An end-to-end retail analytics project combining synthetic and scraped data to analyze pricing, stock availability, and competitor positioning.

## 🚀 Features

* Web scraping using BeautifulSoup
* AI-powered data cleaning using OpenAI GPT
* Data merging and transformation
* Geospatial mapping (lat/lng)
* Anomaly detection using Z-score
* Power BI dashboard for insights

## 🛠 Tech Stack

Python, Pandas, BeautifulSoup, OpenAI API, SciPy, Power BI

## 📊 Key Insights

* Identified pricing anomalies across regions
* Compared competitor pricing
* Detected stock shortages
* Built interactive dashboard

## ▶️ How to Run

1. Install requirements:
   pip install -r requirements.txt

2. Run scripts:
   python scripts/scrape.py
   python scripts/clean_with_gpt.py
   python scripts/merge_data.py
   python scripts/geocode.py
   python scripts/anomaly_detection.py

3. Open Power BI and load:
   data/final_data.csv
