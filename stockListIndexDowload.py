import pandas as pd
#from datetime import datetime
import os
#import time
import subprocess

index = 'VN30_list'
start = '01/01/2016'
end = '08/10/2020'


df = pd.read_csv('general_index/HOSE_index/'+index+".csv")

list_stickers = list(df['sticker']) # Get all sticker in indexes
available_sticker = [fileName.split('.')[0] for fileName in os.listdir('data/')] # get sticker downloaded in data folder
download_sticker = [sticker for sticker in list_stickers if (sticker not in available_sticker)] # Subtract sticker_dowloaded from list ticker to download

def download_stock(stickers,start,end):
    for sticker in stickers:
        subprocess.Popen(["python","download_stock.py",sticker,start,end])

download_stock(download_sticker,start,end)