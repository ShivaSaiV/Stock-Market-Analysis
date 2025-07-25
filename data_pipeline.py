import yfinance as yf
import pandas as pd 

sp500 = "^GSPC"
start_date = "2015-01-01"
end_date = "2025-07-24"

sp500_data = yf.download(sp500, start=start_date, end=end_date)

sp500_data.head()

# Convert to dataframe
sp500_historical_df = pd.DataFrame(sp500_data)

# Save to file
sp500_historical_df.to_csv("sp500_historical.csv", index=False)
