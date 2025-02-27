from requests_html import HTMLSession
import pandas as pd

# Define the URL containing Tesla's revenue data
url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'

# Create an HTML session to mimic a browser request
session = HTMLSession()

# Send a GET request to the URL
response = session.get(url)

# Render the JavaScript content, waiting 5 seconds for the page to load fully
response.html.render(sleep=5)

# Extract the rendered HTML
html = response.html.html

# Extract the table containing 'Quarterly Revenue'
tesla_revenue = pd.read_html(html, match='Quarterly Revenue')[0]

# Clean the 'Revenue' column: remove '$' and ',' and convert to float
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace('$', '').str.replace(',', '').astype(float)

# Display the last five rows of the dataframe
print(tesla_revenue.tail())