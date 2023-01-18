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

#merge VWAP data with tweet count, finalize fact table
def fact_table(df1, df2):
    main_df = df1.merge(right = df2, how = 'left', on = ['Date', 'Stock Name'])
    main_df['tweet_count'] = main_df['tweet_count'].fillna(0)
    main_df = main_df.rename(columns={"Stock Name": "CompanyKey"})
    main_df['RecordKey'] = str(main_df['Date']) + main_df['CompanyKey']
    primary_key = main_df.pop('RecordKey')
    main_df.insert(0, primary_key.name, primary_key)
    return main_df

