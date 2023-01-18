import pandas as pd

#create company dim table
def dimCompany(df, df2):
    df = df['Stock Name'].drop_duplicates().to_frame()
    df2 = df2[['Stock Name', 'Company Name']].drop_duplicates()
    merge_df = df.merge(df2, how = 'left', on = 'Stock Name')
    return merge_df

#create date dim table
def dimDate(df):
    df = df['Date'].to_frame().drop_duplicates()
    df['Day'] = df['Date'].dt.day
    df['Week'] = df['Date'].dt.isocalendar().week
    df['Month'] = df['Date'].dt.month
    df['Quarter'] = df['Date'].dt.quarter
    df['Year'] = df['Date'].dt.year
    df['WeekDay'] = df['Date'].dt.dayofweek
    return df

