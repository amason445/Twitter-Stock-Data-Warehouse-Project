import sqlite3
import pandas as pd

#function to create sqlite file and load tables
def loadTables(output_path, factStockTweets, dimCompany, dimDate):
    con = sqlite3.connect(output_path)
    factStockTweets.to_sql('factStockTweets', con, if_exists = 'replace')
    dimCompany.to_sql('factStockTweets', con, if_exists = 'replace')
    dimDate.to_sql('factStockTweets', con, if_exists = 'replace')
    con.close()
