import pandas as pd
import os
path='temp/'
tickers = [fileName.split('.')[0] for fileName in os.listdir(path) if fileName.endswith('.csv')] 
#ticker = 'ANV'
count =0
for ticker in tickers:
    mdf = pd.read_csv(f'temp/{ticker}.csv')
    df = pd.read_csv(f'data/{ticker}.csv')

    last_date = df['date'][0]
    # Test if last adj_close still == new adj_close
    # or in update time do ticker have pay dividend or split stock
    new_adj = mdf.loc[mdf['date'] == last_date]['adj_close'].values[0]
    old_adj = df['adj_close'][0]
    #last_date = pd.to_datetime(df.index[0]).strftime('%Y-%m-%d')
    if(new_adj == old_adj):
        df1 = pd.concat([df,mdf],axis=0,join='inner',ignore_index=True)
        df1.drop_duplicates(subset='date',keep='first')
        df1['date'] = pd.to_datetime(df1['date'])
        df1 = df1.sort_values(by=['date'])
        df1.to_csv(f'data/{ticker}.csv',index=False)
        '''try:
            os.remove('temp/{ticker}.csv')
        except OSError:
            pass
        '''
        print(f'Complete merge ticker: {ticker}')
        count = count + 1
    else:
        print(f'Ticker {ticker} have modified adj_close and can not update!')
print(f'Finish merge. Success: {count}. Unsuccess: {len(tickers)-count} ')