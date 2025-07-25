import yfinance as yf
import pandas as pd

# List of companies in S&P500
sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
tickers = pd.read_html(sp500_url)[0]['Symbol'].str.replace('.', '-', regex=False).tolist()

# issue: wideformat download
data = yf.download(tickers, period="10y", auto_adjust=False)

# Stack to pivot columns 
long_format_data = data.stack(level=1).rename_axis(['Date', 'Ticker']).reset_index()


long_format_data.to_csv('sp500_historical.csv', index=False)

print(long_format_data.head())