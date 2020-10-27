#from download_stock import *
import pandas as pd
#from datetime import datetime
import os
import time
import subprocess

index = 'VNMID_list'
start = '01/01/2016'
end = '08/10/2020'

path = 'VNMIDCAP/'
df = pd.read_csv('general_index/HOSE_index/'+index+".csv")

list_stickers = list(df['sticker']) # Get all sticker in indexes
available_sticker = [fileName.split('.')[0] for fileName in os.listdir('data/')] # get sticker downloaded in data folder
download_sticker = [sticker for sticker in list_stickers if (sticker not in available_sticker)] # Subtract sticker_dowloaded from list ticker to download
print("Sticker remain:", len(download_sticker),":")
print(",".join(download_sticker))
def download_stock(stickers,start,end):
    for sticker in stickers:
        print("Downloading ...",sticker)
        subprocess.Popen(["python","download_stock.py",sticker,start,end])
        time.sleep(60)
        

download_stock(download_sticker,start,end)