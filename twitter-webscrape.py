# https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-20.php
# Philip Vukovic
# December 10 2019

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

def write_user(handle, writer):
    driver = webdriver.Chrome()
    driver.base_url = "https://twitter.com/" + handle
    driver.get(driver.base_url)
    tweet_count = 0

    while tweet_count < 300:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html_source = driver.page_source
        sourcedata = html_source.encode('utf-8')
        bs = BeautifulSoup(sourcedata, 'lxml')
        all_tweets = bs.find_all('div', {'class':'tweet'})

        if all_tweets:
            tweet_count += len(all_tweets)
            for tweet in all_tweets:
                content = tweet.find('div',{'class':'content'})
                header = content.find('div',{'class':'stream-item-header'})
                user = header.find('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
                message_raw = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
                message = re.sub(r'https?:\/\/.*[\r\n]*', '', message_raw, flags=re.MULTILINE)

                writer.writerow({'author': handle, 'message': message})


csvfile = open('tweets.csv', 'w', newline='', encoding='utf-8')
fields = ['author', 'message']
writer = csv.DictWriter(csvfile, fields)
writer.writeheader()
write_user('@JoeBiden', writer)
write_user('@ewarren', writer)
write_user('@BernieSanders', writer)
write_user('@PeteButtigieg', writer)
write_user('@AndrewYang', writer)
write_user('@amyklobuchar', writer)
write_user('@TomSteyer', writer)
write_user('@MikeBloomberg', writer)
write_user('@realDonaldTrump', writer)

