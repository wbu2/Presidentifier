# https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-20.php

from bs4 import BeautifulSoup
import requests
import csv
import re, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

handle = "@BarackObama"
ctr = 1000

driver = webdriver.Chrome()
driver.base_url = "https://twitter.com/" + handle
driver.get(driver.base_url)

for i in range(1,10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

html_source = driver.page_source
sourcedata = html_source.encode('utf-8')
bs = BeautifulSoup(sourcedata, 'lxml')
all_tweets = bs.find_all('div', {'class':'tweet'})

if all_tweets:
    with open('tweets.csv', 'w', newline='') as csvfile:
        fields = ['author', 'message']
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        first_id = all_tweets[0]['data-item-id']
        last_id = all_tweets[len(all_tweets)-1]['data-item-id']
        
        for tweet in all_tweets[:ctr]:
            content = tweet.find('div',{'class':'content'})
            header = content.find('div',{'class':'stream-item-header'})
            user = header.find('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
            message_raw = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
            message = re.sub(r'https?:\/\/.*[\r\n]*', '', message_raw, flags=re.MULTILINE)

            writer.writerow({'author': handle, 'message': message})

