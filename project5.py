import pandas as pd
import matplotlib.pyplot as plt

# Try to load the data
try:
    data = pd.read_csv('GME_stock_data.csv')
except FileNotFoundError:
    print("Error: The file 'GME_stock_data.csv' was not found. Please check the file path and name.")
    exit()

# Convert the Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label='GameStop Stock Price', color='blue')
plt.title('GameStop Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()