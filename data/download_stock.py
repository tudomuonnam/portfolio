from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException,WebDriverException,StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
#import random
import os
import time
import pandas as pd
import sys

chrome_options = Options()
chrome_options.add_argument('ignore-certificate-errors') #Configure chrome options
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

#stickers = ['VN30INDEX','REE','HCM','PNJ','FMC']
#sticker = random.choice(stickers)
sticker = sys.argv[1]
start = '01/01/2016'
end = '01/10/2020'
# Delete file if exist
try:
    os.remove(sticker+".csv")
except OSError:
    pass

url = 'https://s.cafef.vn/Lich-su-giao-dich-'+sticker+'-1.chn#data'
driver.get(url)
WebDriverWait(driver,5)

start_date = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ctl03_dpkTradeDate1_txtDatePicker"]')
end_date = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ctl03_dpkTradeDate2_txtDatePicker"]')
start_date.send_keys(start)
end_date.send_keys(end)
driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ctl03_btSearch"]').click()
WebDriverWait(driver,2)

while True:
    try:
      #  next_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[title^=' Next to']")))
        ## Find and extract data
        tbl = driver.find_element_by_xpath('//*[@id="GirdTable2"]').get_attribute('outerHTML')
        df = pd.read_html(tbl)
        #refine data
        mdf = df[0]
        if(len(sticker) > 3): 
            cols = [0,8,9,10,1,4]
        else: 
            cols = [0,9,10,11,2,1,5]
        mdf = mdf[mdf.columns[cols]]
        #print(mdf.head())
        mdf = mdf.drop([0,1])
        mdf.to_csv(sticker+".csv",mode='a',header=False,index=False)
        #df = pd.concat([df,mdf],ignore_index=True)
        ## End of extract
        script = driver.find_element_by_css_selector("[title^=' Next to']").get_attribute('href').split(":")[1]
        driver.execute_script(script)
        time.sleep(1)
        driver.execute_script(script)
        time.sleep(1)
        #driver.execute_script(script)
    except NoSuchElementException:
        break
if(len(sticker) > 3): 
    names = ['date','open','high','low','close','volume']
else: 
    names = ['date','open','high','low','close','adj_close','volume']
df = pd.read_csv(sticker+".csv",header=None)
df.columns = names
df['date'] = pd.to_datetime(df['date'])
df.insert(0,'name',sticker)
df.to_csv(sticker+".csv",index=False)

driver.close()
driver.quit()