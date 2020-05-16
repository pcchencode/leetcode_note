import sys, os
import pandas as pd
import random,time
from selenium import webdriver  # 從library中引入webdriver
# from selenium.webdriver.common.by import By
# from fake_useragent import UserAgent # !pip install fake-useragent
from selenium.webdriver.chrome.options import Options
import urllib
# import argparse
# pd.set_option('display.max_rows', 250)

class Chrome(object): # defint a object called chrome
    def __init__(self, width=800, height=600):
        platform = sys.platform
        if platform == 'darwin':
            self.os = 'MAC OS X'
        elif platform == 'win32' or platform == 'cygwin':
            self.os = 'windows'
        elif platform == 'linux':
            self.os = 'linux'

        try:
            if self.os == 'MAC OS X':
                self.driver = webdriver.Chrome('./chromedriver')
            elif self.os == 'windows':
                self.driver = webdriver.Chrome('./chromedriver.exe')
        except Exception as e:
            print(e)
            os._exit(0)

        self.driver.set_window_size(width, height)

        self.version = self.driver.capabilities['chrome']['chromedriverVersion'] # 顯示 chrome driver 版本
        self.name = '555'

        return 

    def open_website(self, url):
        url = str(url)
        self.driver.get(url)

        return

    def google_search(self, key_word):
        key_word = str(key_word)
        self.driver.get('https://www.google.com/')
        search_bar = self.driver.find_element_by_xpath("//input[@class='gLFyf gsfi']") # search bar 的位置
        search_bar.send_keys(key_word)
        search_bar.submit()

        return


a = Chrome()
a.driver.get('https://health.businessweekly.com.tw/event/2020/pediatrics/search.html?keywords=張虔熙&zipcode=0&page=1') #進入投票網站
vote_button = a.driver.find_element_by_xpath("//[@id='search'][@src='dist/img/btn_vote_desktop.png']")
vote_button.click()


# //*[@id="search"]/section[3]/div[1]/div[1]/div[2]/a/picture/img

#a.google_search('how do you turn this on')
#print(a.name)
# print(a.version)
# a.open_website('https://www.instagram.com/nanaciaociao/?hl=zh-tw')


# webdriver.Chrome('./chromedriver')
# a = webdriver.Chrome('./chromedriver')
# a.get('https://www.google.com/')
# button = a.find_element_by_xpath("//input[@class='gLFyf gsfi']")
# button.send_keys(123)
# button.submit()

