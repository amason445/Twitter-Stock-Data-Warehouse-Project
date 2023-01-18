import pandas as pd

#use file path to extract raw twitter csv and clean dates
def twitter_raw(twitter_path):
    tweet_data = pd.read_csv(twitter_path)
    tweet_data['Date'] = tweet_data['Date'].str.split('+').str[0]
    tweet_data['Date'] = pd.to_datetime(tweet_data['Date'], format='%Y-%m-%d %H:%M:%S')
    return tweet_data

#use file path to extract raw stock csv and clean dates
def stock_raw(stock_path):
    stock_data = pd.read_csv(stock_path)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'], format = '%Y-%m-%d')
    return stock_data
