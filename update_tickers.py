import pandas as pd
import datetime 
import time,os
import random
from download_stock_v2 import download_stock
today_date = datetime.date.today()
df = pd.read_csv('report/tickerstatus.csv',parse_dates=['last date'])
path = 'temp/'
available_tickers = [fileName.split('.')[0] for fileName in os.listdir(path) if fileName.endswith('.csv')] 
print('Remaining ',len(df.index)-len(available_tickers),' stock')
for ticker, last_date in zip(df['ticker'].values,pd.to_datetime(df['last date'].values)):
    if((ticker not in available_tickers) and (today_date > last_date)):
        start_date = last_date.strftime('%d/%m/%Y')
        end_date = today_date.strftime('%d/%m/%Y')
        print('Dowloading stock ...',ticker,start_date,end_date)
        try:
            download_stock(ticker,path,start_date,end_date)
        except:
            print('Downloading error',ticker)
            pass
        delay = random.randint(1,4)
        time.sleep(delay)
    


