import yfinance as yf
import matplotlib.pyplot as plt

# Fetch Tesla stock data
tesla_data = yf.Ticker("TSLA").history(period="max")

# Reset the index to make 'Date' a column
tesla_data.reset_index(inplace=True)

# Define the make_graph function
def make_graph(data, title):
    plt.figure(figsize=(12, 6))  # Set figure size
    plt.plot(data['Date'], data['Close'], label='Close Price')  # Plot closing price over time
    plt.title(title)  # Set the title
    plt.xlabel('Date')  # Label for x-axis
    plt.ylabel('Price (USD)')  # Label for y-axis
    plt.legend()  # Add a legend
    plt.grid(True)  # Add a grid for readability
    plt.show()  # Display the plot

# Call the function with Tesla stock data and a title
make_graph(tesla_data, 'Tesla Stock Closing Price Over Time')