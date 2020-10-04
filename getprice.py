from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys

import pandas as pd

chrome_options = Options()
chrome_options.add_argument('ignore-certificate-errors') #Configure chrome options
chrome_options.add_argument('--headless')

brower = webdriver.Chrome(options=chrome_options)

sticker = 'SSI'

url = 'https://s.cafef.vn/Lich-su-giao-dich-'+sticker+'-1.chn#data'


brower.get(url)
WebDriverWait(brower,10)
print(url)
print(brower.title)

start = '01/01/2020'
end = '30/09/2020'

start_date = brower.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ctl03_dpkTradeDate1_txtDatePicker"]')
end_date = brower.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ctl03_dpkTradeDate2_txtDatePicker"]')
start_date.send_keys(start)
end_date.send_keys(end)
brower.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ctl03_btSearch"]').click()
WebDriverWait(brower,10)
## Lay data
tbl = brower.find_element_by_xpath('//*[@id="GirdTable2"]').get_attribute('outerHTML')
df = pd.read_html(tbl)
mdf = df[0]
cols = [0,9,10,11,2,1,5]
mdf = mdf[mdf.columns[cols]]
#print(mdf.head())
mdf = mdf.drop([0,1])
# Change name columns
names = ['date','open','high','low','close','adj_close','volume']
mdf.columns = names
mdf.index = pd.to_datetime(mdf['date'])
del mdf['date']
mdf.to_csv('mssi.csv')
brower.close()
brower.quit()