from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException,WebDriverException,StaleElementReferenceException,UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pandas as pd
import sys

chrome_options = Options()
chrome_options.add_argument('ignore-certificate-errors') #Configure chrome options
chrome_options.add_argument('--headless')
#start_date = '2015-07-24'
def copydate(start,end):
    df = pd.read_csv('data/VNINDEX.csv')
    df.index = pd.to_datetime(df['date'],format='%Y-%m-%d')
    df = df.sort_index()
    df = df[start:end]
    mydate_list = df.index.tolist()
    return mydate_list

def get_TRI_index(mdate):
    #global df
    mdate = mdate.strftime('%d.%m.%Y')
    date_field = driver.find_element_by_xpath('//*[@id="TradingDate"]')
    date_field.clear()
    date_field.send_keys(mdate)
    driver.find_element_by_xpath('//*[@id="etfPriceTradingSummaryCriteria"]/tbody/tr/td[2]/a').click()
    time.sleep(1)
    my_arr = [0,0,0,0,0,0,0,0]
    try:
        tbl = driver.find_element_by_xpath('//*[@id="id-data-tri"]').get_attribute('outerHTML')

    except UnexpectedAlertPresentException:
        print(mdate)
        pass
    else:
        try: 
            data = pd.read_html(tbl)
        except ValueError:
            print(mdate)
            pass
        data = data[0]
        data['value'] = [ x*1000 if x < 10 else x/100 for x in data[1]]
        my_arr = data['value'].tolist()
        
    my_arr.insert(0,mdate)
    return my_arr

cols = ['date', 'VN30 TRI', 'VNMID TRI', 'VNSML TRI', 'VN100 TRI', 'VNALL TRI', 'VNDIAMON TRI', 'VNFINLEA TRI', 'VNFINSEL TRI']
df = pd.DataFrame(columns =cols)
start_date = '2020-01-01'
end_date = '2020-12-31'

driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.hsx.vn/Modules/Listed/Web/TriIndexView/'
driver.get(url)
WebDriverWait(driver,2)

list_date = copydate(start_date,end_date)
for mdate in list_date:
    my_arr = get_TRI_index(mdate)
    df = df.append(pd.Series(my_arr,index=cols),ignore_index=True)

df.to_csv('TRI_index-'+start_date+'-'+end_date+'.csv')

driver.close()
driver.quit()

'''
try: 
    tbl = driver.find_element_by_xpath('//*[@id="id-data-tri"]')
except UnexpectedAlertPresentException:
    pass
'''