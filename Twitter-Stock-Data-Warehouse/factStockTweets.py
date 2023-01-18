import pandas as pd

#create twitter count data frame
def count_tweets(df):
    df = df.groupby([pd.Grouper(key = 'Date', freq = 'M'), 'Stock Name'])['Tweet'].count()
    df = df.reset_index()
    df = df.rename(columns={"Tweet": "tweet_count"})
    return df

#create stock VWAP dataframe
def stock_frame(df):
    df['typical_price'] = (df['Low'] + df['High'] + df['Adj Close']) / 3
    df = df.groupby([pd.Grouper(key = 'Date', freq = 'M'), 'Stock Name']).apply(
            lambda df: sum((df['typical_price'] * df['Volume']))/sum(df['Volume']))
    df = df.reset_index(name = 'VWAP')
    return df
    

