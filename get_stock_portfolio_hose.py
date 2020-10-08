from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
#import csv
import time
#class get_index()
chrome_options = Options()
chrome_options.add_argument('ignore-certificate-errors') #Configure chrome options
chrome_options.add_argument('--headless')

VN30 = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/1964531007'
VNALL = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/951937685'
VNMID = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/699240157'
VNSI = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/'
VNSML = 'https://www.hsx.vn/Modules/Listed/Web/StockIndexView/434493689'


url = VNSML
def get_stock_list(url):
    drive = webdriver.Chrome(options=chrome_options)
    drive.get(url)
    #WebDriverWait(drive,20)
    time.sleep(25)
    #tbl = drive.find_element_by_id('hose-indecies-grid').get_attribute('outerHTML')
    tbl = drive.find_element_by_xpath('//*[@id="gview_hose-indecies-grid"]/div[3]').get_attribute('outerHTML')
    df = pd.read_html(tbl)[0]
    drive.quit()
    df = df.drop([0])
    df = df[df.columns[[1,4]]]
    df.columns = ['sticker','name']
    df.drop_duplicates(subset='sticker',keep='first')  # Delete duplicate
    return df
