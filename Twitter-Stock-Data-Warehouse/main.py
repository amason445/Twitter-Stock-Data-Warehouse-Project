import os
import pandas as pd

# This file extracts twitter and stock data and loads into a SQLite data warehouse

# Define file paths to raw data
tweet_path = os.path.join(os.path.expanduser('~'), 'Twitter-Stock-Data-Warehouse', 'SourceData', 'stock_tweets.csv')
stock_path = os.path.join(os.path.expanduser('~'), 'Twitter-Stock-Data-Warehouse', 'SourceData', 'stock_yfinance_data.csv')

#create data frames from raw data
tweet_data = pd.read_csv(tweet_path)
stock_data = pd.read_csv(stock_path)

tweet_data.info()


