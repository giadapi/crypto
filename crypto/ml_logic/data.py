"""
This module is downloading the Bitcoin price and twitter data from API
"""

# import pandas as pd
import yfinance as yf
# import datetime

#Part A - Download the Crytoprice from Yahoo Finance API
"""
- Example of symbol:
'BTC-USD','ETH-USD','BCH-USD','LTC-USD','BNB-USD','BAT-USD','XLM-USD',
'DOGE-USD','DOGE-USD','COMP-USD','ALGO-USD','OMG-USD'
- Example of start_date_str: 2022-06-24
- Example of end_date_str: 2023-03-08
- Example of period: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
- Example of intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
"""
def load_historic_data(symbol, start_date_str, end_date_str, period, interval):
    try:
        df = yf.download(symbol, start=start_date_str, end=end_date_str, period=period, interval=interval)
        #  Add symbol
        df["Symbol"] = symbol
        df['price_change'] = df['Close'].pct_change()
        return df
    except:
        print(f'Error loading stock data for + {symbol}')
        return None

#Part B - Download the twitter data from twitter
