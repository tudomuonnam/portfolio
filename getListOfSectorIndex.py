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
drive = webdriver.Chrome(options=chrome_options)
def get_stock_list(sticker,url):
    drive = webdriver.Chrome(options=chrome_options)
    drive.get(url)
    #WebDriverWait(drive,20)
    time.sleep(35)
    #tbl = drive.find_element_by_id('hose-indecies-grid').get_attribute('outerHTML')
    tbl = drive.find_element_by_xpath('//*[@id="sector-indecies"]').get_attribute('outerHTML')
    df = pd.read_html(tbl)[1]
    drive.quit()
    df = df.drop([0])
    df = df[df.columns[[1,4]]]
    df.columns = ['sticker','name']
    df.drop_duplicates(subset='sticker',keep='first')  # Delete duplicate
    df.to_csv('general_index/Sector_index/'+sticker+'.csv')
    return df

def get_list_portfolio_index(url): # Tra về bảng gồm bộ chỉ số VNIndex
    #url = 'https://www.hsx.vn/Modules/Listed/Web/SectorIndexView/?fid=218ca2db035948beac048d862ac03d30' #Sector index
    drive = webdriver.Chrome(options=chrome_options)
    drive.get(url)
    time.sleep(15)
    tbl = drive.find_element_by_xpath('//*[@id="sector-indecies-grid"]').get_attribute('outerHTML') # //*[@id="sector-indecies-grid"]
    # Get all link from page
    elements = tbl.find_elements_by_xpath('//*[@href]')
    # Disconnect drive
    drive.close()
    dirve.quit()
    # Keep link in list
    links = [element.get_attribute('href') for element in elements]
    # Filter links contain "Listed/Web/SectorItemView"
    links = [link for link in links if ("Listed/Web/SectorItemView" in link)]
    # Get table as usual
    df = pd.read_html(tbl)[0]
    df = df.drop([0])
    df = df[df.columns[[0,1,2]]]
    df.columns = ['indexs','name','numberOfStock']
    # Copy links to dataframe
    df['link'] = ''
    for i in range(len(links)): df['link'][i+1] = links[i]
    return df
    #df.to_csv('general_index/Sector_index/sectorIndex.csv')
for i in range(len(df)):
    sticker,url = df['indexs'][i],df['link'][i]
    get_stock_list(sticker,url)