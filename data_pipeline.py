import yfinance as yf
import pandas as pd 

# Load from wikipedia
wikipedia_link = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
sp500 = pd.read_html(wikipedia_link)[0]

# Extract symols
sp500_symbols = sp500["Symbol"].tolist()
print(len(sp500_symbols))

# Get from yfinance
sp500_data = yf.download(sp500_symbols, period="10y", group_by='ticker', auto_adjust=False)
print(sp500_data.head())

# Save to CSV file
sp500_data.to_csv("sp500_historical.csv")