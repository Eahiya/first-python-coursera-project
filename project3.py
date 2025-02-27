import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL for GameStop revenue data
url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'

# Set headers to mimic a browser request and avoid blocking
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Initialize an empty list to store the data
data = []

# Find the table containing "GameStop Quarterly Revenue"
for table in soup.find_all('table'):
    if table.find('th') and table.find('th').getText().startswith("GameStop Quarterly Revenue"):
        # Extract rows from the table body
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) == 2:  # Ensure the row has exactly 2 columns (Date and Revenue)
                date = col[0].text.strip()
                revenue = col[1].text.strip().replace("$", "").replace(",", "")
                data.append({"Date": date, "Revenue": revenue})

# Create the DataFrame from the collected data
if data:
    gme_revenue = pd.DataFrame(data)
    # Display the last five rows
    print(gme_revenue.tail())
else:
    print("No data found")