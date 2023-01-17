import os
import pandas as pd

# This file extracts twitter and stock data and loads into a SQLite data warehouse

# Define file paths to raw data
tweet_path = os.path.join(os.path.expanduser('~'), 'Twitter-Stock-Data-Warehouse', 'SourceData', 'stock_tweets.csv')
stock_path = os.path.join(os.path.expanduser('~'), 'Twitter-Stock-Data-Warehouse', 'SourceData', 'stock_yfinance_data.csv')

#create data frames from raw data
tweet_data = pd.read_csv(tweet_path)
stock_data = pd.read_csv(stock_path)

#convert tweet date columns into datetime format
tweet_data['Date'] = tweet_data['Date'].str.split('+').str[0]
tweet_data['Date'] = pd.to_datetime(tweet_data['Date'], format='%Y-%m-%d %H:%M:%S').dt.date

#convert stock data columns into datetime format
stock_data['Date'] = pd.to_datetime(stock_data['Date'], format = '%Y-%m-%d').dt.date

print(stock_data.head(5))

