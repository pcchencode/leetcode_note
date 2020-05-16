import sys, os
import pandas as pd
import random,time
from selenium import webdriver  # 從library中引入webdriver
# from selenium.webdriver.common.by import By
from fake_useragent import UserAgent # !pip install fake-useragent
from selenium.webdriver.chrome.options import Options
import urllib
# import argparse
# pd.set_option('display.max_rows', 250)

class Chrome(object): # defint a object called chrome
    def __init__(self, width=800, height=600, user_agent=False):
        platform = sys.platform
        if platform == 'darwin':
            self.os = 'MAC OS X'
        elif platform == 'win32' or platform == 'cygwin':
            self.os = 'windows'
        elif platform == 'linux':
            self.os = 'linux'

        options = Options()
        if user_agent==True:
            ua = UserAgent()
            user_agent = ua.random
            print(user_agent)
            options.add_argument(f'user-agent={user_agent}')

        try:
            if self.os == 'MAC OS X':
                self.driver = webdriver.Chrome('./chromedriver', options=options)
            elif self.os == 'windows':
                self.driver = webdriver.Chrome('./chromedriver.exe', options=options)
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


def loop_voting(n):
    done_num = 0
    remained = n
    try:
        while remained > 0:
            print('step remained '+str(remained))
            time.sleep(random.randint(1,2))
            
            ua = UserAgent()
            user_agent = ua.random
            options = Options()
            options.add_argument("window-size=800,800")
            options.add_argument(f'user-agent={user_agent}')
            print(user_agent)

            browser = webdriver.Chrome('./chromedriver', chrome_options=options)
            browser.get('https://health.businessweekly.com.tw/event/2020/pediatrics/search.html?keywords=張虔熙&zipcode=0&page=1')
            time.sleep(random.randint(8,10))

            vote_button = browser.find_element_by_xpath("//*[@id='search']/section[3]/div[1]/div[1]/div[2]/a/picture/img")
            vote_button.click()
            time.sleep(random.randint(5,10))
            
            check_box_pro = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[1]/label')
            check_box_nice = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[2]/label')
            check_box_detail = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[3]/label')
            check_box_med = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[4]/label')
            
            checkbox_list = [check_box_pro, check_box_nice, check_box_detail, check_box_med]

            pick = random.randint(1,4)
            chosen_checkbox = random.choices(checkbox_list, k=pick)

            for val in chosen_checkbox:
                val.click()
            
#             check_box_pro = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[1]/label')
#             check_box_pro.click()

#             check_box_nice = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[2]/label')
#             check_box_nice.click()

#             check_box_detail = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[3]/label')
#             check_box_detail.click()

#             check_box_med = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[4]/label')
#             check_box_med.click()
            time.sleep(5)
            submit_button = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[3]/a[1]')
            submit_button.click()

            browser.close()

            time.sleep(random.randint(1,5))
            remained = remained-1
            done_num = done_num+1
    except:
        browser.close()
        print('stop at step ' + str(done_num))
        print('restart')
        return loop_voting(remained)

loop_voting(n=10)


# a = Chrome(user_agent=True)
# a.driver.get('https://health.businessweekly.com.tw/event/2020/pediatrics/search.html?keywords=張虔熙&zipcode=0&page=1') #進入投票網站
# time.sleep(8)
# vote_button = a.driver.find_element_by_xpath("//*[@id='search']/section[3]/div[1]/div[1]/div[2]/a/picture/img")
# time.sleep(5)
# vote_button.click()




