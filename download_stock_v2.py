from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException,WebDriverException,StaleElementReferenceException,UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import random
import os
import time
import pandas as pd
import sys

chrome_options = Options()
chrome_options.add_argument('ignore-certificate-errors') #Configure chrome options
chrome_options.add_argument('--headless')

path = 'temp/'
'''
sticker = sys.argv[1]
if (len(sys.argv) > 2): start = sys.argv[2]
else: start = '01/01/2016'
if (len(sys.argv) > 2): end = sys.argv[3]
else: end = '01/10/2020'
#start = '01/01/2016' if (len(sys.argv[2]) > 1) else sys.argv[2]
#end = '01/10/2020' if (len(sys.argv[3]) > 1) else sys.argv[3]
'''
def download_stock(sticker,path,start,end):
    try:
        os.remove(path+sticker+".csv")
    except OSError:
        pass
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://s.cafef.vn/Lich-su-giao-dich-'+sticker+'-1.chn#data'
    driver.get(url)
    WebDriverWait(driver,5)

    start_date = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ctl03_dpkTradeDate1_txtDatePicker"]')
    end_date = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ctl03_dpkTradeDate2_txtDatePicker"]')
    start_date.send_keys(start)
    end_date.send_keys(end)
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ctl03_btSearch"]').click()
    WebDriverWait(driver,2)
    #while True:
    #    try:
        #  next_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[title^=' Next to']")))
            ## Find and extract data
    try:
        tbl = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/table').get_attribute('outerHTML')
    except StaleElementReferenceException:
        pass
    try:
        df = pd.read_html(tbl)
    except UnboundLocalError:
        df = pd.DataFrame()
        pass
    #refine data
    mdf = df[0]
    if(len(sticker) > 3): 
        cols = [0,8,9,10,1,4,1] #'date','open','high','low','close','volume',adj_close
    else: 
        cols = [0,9,10,11,2,5,1] # date,open,high,low,close,volume,adj_close
    mdf = mdf[mdf.columns[cols]]
    #print(mdf.head())
    mdf = mdf.drop([0,1])
    mdf.to_csv(sticker+".csv",mode='a',header=False,index=False)
            #df = pd.concat([df,mdf],ignore_index=True)
            ## End of extract
            #script = driver.find_element_by_css_selector("[title^=' Next to']").get_attribute('href').split(":")[1]
            #driver.execute_script(script)
            #time.sleep(1)
            #driver.execute_script(script)
            #time.sleep(1)
            #driver.execute_script(script)
       # except NoSuchElementException:
        #    print("Error! Not complete for ", sticker)
        #    pass
    driver.close()
    driver.quit()

    names = ['date','open','high','low','close','volume','adj_close']
    df = pd.read_csv(sticker+".csv",header=None)
    df.columns = names
    df['date'] = pd.to_datetime(df['date'],format='%d/%m/%Y')
    df.insert(0,'name',sticker)

    # If we crawl index, just got adj_close = close price
    if(len(sticker) > 3): 
        df['adj_close'] = df['close']
    # finally drop duplicate if have any
    df = df.drop_duplicates()
    # Save to csv
    df.to_csv(path+sticker+".csv",index=False)
    try:
        os.remove(sticker+".csv")
    except OSError:
        pass
    print("Download complete! See in " + path +sticker+".csv file")
    return df

def download_portfolio(stickers,path,start,end):
    for sticker in stickers:
        download_stock(sticker,path,start,end)

#download_stock(sticker,path,start,end)