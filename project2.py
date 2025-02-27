import yfinance as yf

# Extract GameStop stock data
gme_data = yf.Ticker("GME").history(period="max")

# Reset the index
gme_data.reset_index(inplace=True)

# Display the first five rows
print(gme_data.head())