import os
import sqlite3
import pandas as pd
import precleaning as pre
import fact_table as fact
import dim_tables as dim
import load_tables as load

# This file extracts twitter and stock data and loads into a SQLite data warehouse

# Define file paths to source data
twitter_path = os.path.join(os.path.expanduser('~'), 'Twitter-Stock-Data-Warehouse', 'SourceData', 'stock_tweets.csv')
stock_path = os.path.join(os.path.expanduser('~'), 'Twitter-Stock-Data-Warehouse', 'SourceData', 'stock_yfinance_data.csv')
output_path = os.path.join(os.path.expanduser('~'), 'Twitter-Stock-Data-Warehouse', 'ResultsDW.sqlite')

#create source dataframes
twitter_data = pre.twitter_raw(twitter_path)
stock_data = pre.stock_raw(stock_path)

#build tweet count dataframe
tweet_count = fact.count_tweets(twitter_data) 

#build stock metrics dataframe
stock_metrics = fact.stock_frame(stock_data)

#merge twitter data and stock metrics frame
factStockTweets = fact.fact_table(stock_metrics, tweet_count)

#create dim dataframes
dimCompany = dim.dimCompany(stock_data, twitter_data)
dimDate = dim.dimDate(stock_data)

#load to SQLite Database
load.loadTables(output_path, factStockTweets, dimCompany, dimDate)
