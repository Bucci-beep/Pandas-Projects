import pandas as pd
# Simulate or load daily stock prices (date, open, close, volume)
dates = pd.date_range(start='2025-02-01', periods=5, freq='D')
open_prices = [100, 102, 105, 110, 108]
close_prices = [102, 105, 110, 108, 109]
volumes = [100000, 120000, 130000, 110000, 115000]

stocks = pd.DataFrame({
    'Date': dates,
    'Open': open_prices,
    'Close': close_prices,
    'Volume': volumes
}, index=range(1, len(dates) + 1))

print("\nStock Prices:")
print(stocks)

# Convert date strings to datetime objects
stocks['Date'] = pd.to_datetime(stocks['Date'])
print("\nStock Prices with Date as datetime object:")
print(stocks)

# Calculate daily percentage change in stock prices
stocks['Daily Change'] = (stocks['Close'] - stocks['Open']) / stocks['Open'] * 100
print("\nStock Prices with Daily Percentage Change:")
print(stocks)

# Compute a cumulative return column
stocks['Cumulative Return'] = stocks['Close'].pct_change().cumsum()
print("\nStock Prices with Cumulative Return:")
print(stocks)