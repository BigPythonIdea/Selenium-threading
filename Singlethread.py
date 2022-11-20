# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:18:53 2022

@author: Takodachi
"""

"""
Created on Mon Apr  5 10:26:44 2021
@author: Solana
"""

import pandas as pd
import time
import os
from threading import Thread

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def Threads():
    df = pd.read_csv("company_lst.csv", index_col=0)
    acc= []
    
    for symbol in df["0"]:
        try:
            driver = webdriver.Chrome()
            driver.get("https://mops.twse.com.tw/mops/web/t163sb03")
        except:
            print(str(symbol)+"web error")
        ########################History################################
        select = Select(driver.find_element_by_xpath('//*[@id="isnew"]'))
        select.select_by_value("false")
        
        ########################Symbol################################
        element = driver.find_element_by_xpath('//*[@id="co_id"]')
        element.send_keys(str(symbol))
        
        ########################Year################################
        year = driver.find_element_by_xpath('//*[@id="year"]')
        year.send_keys("104")
        
        ########################Season################################
        season = Select(driver.find_element_by_xpath('//*[@id="season"]'))
        season.select_by_value("04")
        
        ########################Button################################
        button = driver.find_element_by_xpath('/html/body/center/table/tbody/tr/td/div[4]/table/tbody/tr/td/div/table/tbody/tr/td[3]/div/div[3]/form/table/tbody/tr/td[4]/table/tbody/tr/td[2]/div/div/input').click()
        
        ##wait web load 2sec
        time.sleep(2)
        
        try:
            acc.append(driver.find_element_by_xpath('//*[@id="table01"]/table[4]/tbody/tr[4]').text) 
            driver.close()
            df = pd.DataFrame(acc)
            df.to_csv(os.getcwd()+"\\test\\"+str(symbol)+".csv", encoding="utf_8_sig")
        except :
            print(str(symbol)+"Not Element")
            
    
        time.sleep(5)
        
Thread_Team = []
for x in range(10):
    t = Thread(target=Threads)
    t.start()
    Thread_Team.append(t)

for t in Thread_Team:
    t.join()