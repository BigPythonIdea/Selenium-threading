# -*- coding: utf-8 -*-
"""
多線程爬蟲
https://blog.csdn.net/qq_52914337/article/details/123161038
"""

import pandas as pd
import time
import os

import threading
# from threading import Thread

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def blueprint(years):
    strat_time = time.time()
    df = pd.read_csv("testtime.csv", index_col=0)
    acc= []
  
    for symbol in df["0"]:
      for y in years:
          try:
              driver = webdriver.Chrome()
              driver.get("https://mops.twse.com.tw/mops/web/t163sb03")
          except:    
              print(str(symbol)+"web error")
          select = Select(driver.find_element_by_xpath('//*[@id="isnew"]'))  
          select.select_by_value("false")
          
          element = driver.find_element_by_xpath('//*[@id="co_id"]')
          element.send_keys(str(symbol))
          
          year = driver.find_element_by_xpath('//*[@id="year"]')
          year.send_keys(y)
          
          season = Select(driver.find_element_by_xpath('//*[@id="season"]'))
          season.select_by_value("04")
          
          button = driver.find_element_by_xpath('/html/body/center/table/tbody/tr/td/div[4]/table/tbody/tr/td/div/table/tbody/tr/td[3]/div/div[3]/form/table/tbody/tr/td[4]/table/tbody/tr/td[2]/div/div/input').click()
          
          time.sleep(2)
          
          try:
              acc.append(driver.find_element_by_xpath('//*[@id="table01"]/table[4]/tbody/tr[4]').text) 
              driver.close()
              # df = pd.DataFrame(acc)
              # df.to_csv(os.getcwd()+"\\test\\"+str(symbol)+".csv", encoding="utf_8_sig")
          except :
              print(str(symbol)+"Not Element")
          time.sleep(5)
    end_time = time.time()
    print('用時%f' % (end_time-strat_time))

def task1():
    lst = ["104","105","106"]
    t1 = blueprint([i for i in lst])
    time.sleep(2)

def task2():
    lst = ["107","108","109","110"]
    t2 = blueprint([i for i in lst])
    time.sleep(2)


def multi_thread():
    thr1 = threading.Thread(target=task1)
    thr2 = threading.Thread(target=task2)
    thr1.start()
    thr2.start()



  
if __name__ == "__main__":
    strat_time = time.time()
    multi_thread()
    


    
        