import sqlite3
import pandas as pd

'''
sticker = 'SSI'
file = "data/" + sticker + ".csv" 
df = pd.read_csv(file)
df['date'] = pd.to_datetime(df['date'])
df.index = df['date']
'''
def get_price(sticker):
    file = "data/" + sticker + ".csv" 
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['date'])
    df.index = df['date']
    return df