# data_loader.py
import yfinance as yf
import pandas as pd
import numpy as np
import os

def get_data(tickers, start="2015-01-01", end="2025-01-01"):
    """Download adjusted close prices for selected tickers."""
    data = yf.download(tickers, start=start, end=end)["Close"]
    data = data.dropna(how="all")  # remove empty rows
    return data

def compute_returns(prices):
    """Compute daily log returns."""
    returns = np.log(prices / prices.shift(1))
    return returns.dropna()

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "META", "TSLA", "NVDA"]

    # make sure data folder exists
    os.makedirs("data", exist_ok=True)

    # fetch prices
    prices = get_data(tickers)
    returns = compute_returns(prices)

    # preview
    print("Prices sample:")
    print(prices.tail())
    print("\nReturns sample:")
    print(returns.tail())

    # save locally
    prices.to_csv("data/magnificent7_prices.csv")
    returns.to_csv("data/magnificent7_returns.csv")

    print("\nData saved successfully!")


