import pandas as pd
import os,path
path = 'data/'
tickers = [fileName.split('.')[0] for fileName in os.listdir(path) if fileName.endswith('.csv')] 
#mdf = pd.DataFrame(index=['tickers','first data','last date','last adj close'])
my_list = []
for ticker in tickers:
    df = pd.read_csv(path+ticker+'.csv')
    data = [ticker,df['date'].iloc[-1],df['date'].iloc[0],df['adj_close'].iloc[0],len(df.index)]
    my_list.append(data)
mdf = pd.DataFrame.from_dict(my_list)
mdf.columns = ['ticker','last date','start date','last adj close','Lines']
mdf.to_csv('report/tickerstatus.csv',index=False)
print('Check status finish! Complete ',len(tickers),' tickers')