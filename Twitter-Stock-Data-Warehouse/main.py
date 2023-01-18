import os
import pandas as pd
import precleaning as pre
import factStockTweets as fact

# This file extracts twitter and stock data and loads into a SQLite data warehouse

# Define file paths to raw data
twitter_path = os.path.join(os.path.expanduser('~'), 'Twitter-Stock-Data-Warehouse', 'SourceData', 'stock_tweets.csv')
stock_path = os.path.join(os.path.expanduser('~'), 'Twitter-Stock-Data-Warehouse', 'SourceData', 'stock_yfinance_data.csv')

#create data frames from raw data
twitter_data = pre.twitter_raw(twitter_path)
stock_data = pre.stock_raw(stock_path)

#aggregate tweets
tweet_count = fact.count_tweets(twitter_data) 

#build stock metrics data frame
stock_metrics = fact.stock_frame(stock_data)

#merge twitter data and stock metrics frame
fact_table = fact.fact_table(stock_metrics, tweet_count)

fact_table.info()

