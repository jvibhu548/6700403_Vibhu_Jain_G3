import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download Bitcoin Data
btc = yf.download("BTC-USD", start="2020-01-01")

# Download Ethereum Data
eth = yf.download("ETH-USD", start="2020-01-01")

# Save inside data folder
btc.to_csv("data/BTC-USD.csv")
eth.to_csv("data/ETH-USD.csv")

print("Dataset downloaded")


# Cleaning
btc = btc.dropna()
eth = eth.dropna()

btc = btc.sort_index()
eth = eth.sort_index()

btc = btc.rename(columns={"Adj Close": "Adj_Close"})
eth = eth.rename(columns={"Adj Close": "Adj_Close"})


# Daily return (% change)
btc['Daily_Return'] = btc['Close'].pct_change()
eth['Daily_Return'] = eth['Close'].pct_change()

# 7-day moving average
btc['MA_7'] = btc['Close'].rolling(7).mean()
eth['MA_7'] = eth['Close'].rolling(7).mean()

# Volatility (7-day rolling std)
btc['Volatility'] = btc['Daily_Return'].rolling(7).std()
eth['Volatility'] = eth['Daily_Return'].rolling(7).std()


btc.to_csv("cleaned/btc_cleaned.csv")
eth.to_csv("cleaned/eth_cleaned.csv")

print("Cleaned data saved!")



plt.figure(figsize=(12,5))
plt.plot(btc['Close'])
plt.title("Bitcoin Close Price")
plt.show()

plt.figure(figsize=(12,5))
plt.plot(btc['Daily_Return'])
plt.title("Bitcoin Daily Return")
plt.show()

plt.figure(figsize=(12,5))
plt.plot(btc['MA_7'])
plt.title("Bitcoin 7-day Moving Average")
plt.show()

plt.figure(figsize=(12,5))
plt.plot(btc['Volatility'])
plt.title("Bitcoin Volatility (7-day)")
plt.show()
