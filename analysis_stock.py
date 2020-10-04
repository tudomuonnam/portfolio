import pandas as pd
#import datetime as dt
import matplotlib as mpl

stickers = ['VNINDEX','SSI','REE','PVT','HCM']
sticker = 'SSI'
start = '2018-01-01' #dt.date(2018,1,1)
end = '2020-10-01' #dt.date(2020,10,1)

def get_stock(sticker,start='2017-01-01',end='2020-10-02'):
    #sticker = 'SSI'
    #start = '2017-01-01'
    file = "data/" + sticker + ".csv" 
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['date'])
    df.index = df['date']
    del df['date']
    del df['name']
    # Create header 2 layer
    names = df.columns.tolist()
    sub = [sticker for _ in range(len(names))]
    header = [names,sub]
    df.columns = header
    # Filter dataframe with start and end date
    df = df.loc[start:end]
    return df

def get_adj_portfolio(stickers,start_date='2018-01-01',end_date='2020-10-02'):
    df = pd.DataFrame()
    for i in range(len(stickers)):
        if(i==0): 
            sticker = stickers[i]
            df = get_stock(sticker,start_date,end_date)
        else:
            sticker = stickers[i]
            df1 = get_stock(sticker,start_date,end_date)
            df = df.join(df1,how='inner')
    return(df['adj_close'])


