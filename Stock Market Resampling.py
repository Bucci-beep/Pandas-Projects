"""
This script simulates daily stock data and demonstrates:
  - Resampling data to generate weekly and monthly summaries.
  - Filtering data based on volume or price changes.
The functionality here is an extension of the Stock Market Time Series analysis.
"""

import pandas as pd
import numpy as np

# Step 1: Simulate daily stock data
# Create a data range for 30 days
dates = pd.date_range(start='2025-02-01', periods=30, freq='D')

np.random.seed(42)
# Simulate daily data for open, close, and volume

data = {
    'Open': np.random.randint(100, 200, 30),
    'Close': np.random.randint(100, 200, 30),
    'Volume': np.random.randint(100000, 200000, 30)
}

# Create the data frame with date as index
stocks = pd.DataFrame(data, index=dates)
stocks.index.name = 'Date'

# Calculate the daily price change for filtering later
stocks['Price_Change'] = (stocks['Close'] - stocks['Open'])
stocks['Price_Percent_Change'] = (stocks['Price_Change'] / stocks['Open']) * 100

print("\nDaily Stock Prices:")
print(stocks)

# Step 2: Resample data to weekly and monthly summaries
# Weekly summary: Average 'open', and 'close'; total 'volume'
weekly_summary = stocks.resample('W').agg({
    'Open': 'mean',
    'Close': 'mean',
    'Volume': 'sum'
})

print("\nWeekly Stock Summary:")
print(weekly_summary, "\n")

# Monthly summary: Average 'open', and 'close'; total 'volume'
monthly_summary = stocks.resample('ME').agg({
    'Open': 'mean',
    'Close': 'mean',
    'Volume': 'sum',
    'Price_Change': 'sum',
})

print("\nMonthly Stock Summary:")
print(monthly_summary, "\n")

# Step 3: Filter data based on volume or price changes
# Filter out days where the absolute price change is greater than 10
large_price_change = stocks[stocks['Price_Change'].abs() > 10]
print("\nDays with Large Price Changes (> 10):")
print(large_price_change, "\n")

# Filter out days where the volume is above a certain threshold e.g., > 170000
high_volume_days = stocks[stocks['Volume'] > 170000]
print("\nDays with High Volume (> 170000):")
print(high_volume_days, "\n")
