# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:41:16 2020

@author: Jack
"""
import os
import time
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
'''
Imports dependencies required to run this script. Based around selenium webdriver and pandas.
'''
constituents = open(r"C:\Users\Jack\Documents\Professional Docs\SP500Ticks.csv")
'''
Opens list of tickers from the associated csv file.
'''
constitRead = pd.read_csv(constituents)
'''
Reads the file into a pandas dataframe.
'''
ticker = constitRead['Symbol'].tolist()
ticker2 = ticker[58:505]
ticker3 = ticker2[11:447]
ticker4 = ticker3[12:436]
ticker5 = ticker4[277:423]
ticker6 = ticker5[8:145]
'''
Turns the dataframe into a list. Repeated because I am a hack.
'''
tickerlen = len(ticker)
tickerlen2 = len(constitRead[58:505])
tickerlen3 = len(constitRead[69:505])
tickerlen4 = len(constitRead[81:505])
tickerlen5 = len(constitRead[358:505])
tickerlen6 = len(constitRead[366:505])
'''

Counts the length of the ticker list. "^^"
'''

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderlist",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', "text/plain, application/vnd.ms-excel, text/csv, text/comma-separated-values, application/octet-stream")
'''
Sets up the Firefox browser profile to download files with automation.
'''



i = 0 
'''
Initizalizes counter for the program at 0.
'''
for i in range(tickerlen6):
#for i in tickerlen(44:505):
    '''
    Creates the for loop for the ticker list.
    '''
    driver = webdriver.Firefox(firefox_profile = fp)
    driver.get("https://www.finance.yahoo.com")
    '''
    Initializes selenium to open firefox to Yahoo Finance.
    '''
#assert "Finance" in driver.title
    time.sleep(8)
    query = driver.find_element_by_id('yfin-usr-qry')
    queryclick = driver.find_element_by_id('header-desktop-search-button')
    #time.sleep(10)
    '''
    Orders selenium to find the search bar and button for entering tickers
    and waits for the page to load.
    ''' 
    query.send_keys(format(ticker6[i]))
    time.sleep(3)
    queryclick.click()
    '''
    Orders selenium to send the stock tickers to the search bar looping over
    the ticker list for the length of the list. This breaks if Yahoo Finance
    takes too long to load or there are web issues. Modify time.sleep() to
    account for your internet and computing capabilites.
    '''
    #tSLA = query.send_keys(Keys.RETURN)
    #time.sleep(3)
    time.sleep(6)
    histData = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/section/div/ul/li[6]/a/span')
    #time.sleep(6)
    histData.click()
    '''
    Waits for the page ticker's page to laod, finds the historical data
    selector and clicks it.
    '''
    time.sleep(6)
    maxTime = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div/div')
    #newMaxTime = driver.find_element_by_xpath('//span[@data-value="MAX"]')
    time.sleep(3)
    maxTime.click()
    '''
    Finds the dropdown button in the historical data selector and clicks
    it. Accounts for loading time.
    '''
    time.sleep(3)
    maxTimeMax = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div/div/div/div/div/ul[2]/li[4]/button')
    time.sleep(3)
    maxTimeMax.click()
    '''
    Finds the max duration button and clicks it. Accounts for loading.
    
    '''
    time.sleep(3)
    downloadHist = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[2]/span[2]/a')
    time.sleep(3)
    downloadHist.click()
    '''
    Waits for the max duration content to load, finds the download button and
    clicks.
    '''
    time.sleep(4)
    driver.close()
    '''
    Waits for the download to complete and closes the browser.
    '''
i += 1
'''
Increments the loop to run again.
'''