# https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-20.php

from bs4 import BeautifulSoup
import requests
import csv
import re

handle = "@BarackObama"
ctr = 1000

res = requests.get('https://twitter.com/' + handle)
bs = BeautifulSoup(res.content, 'lxml')
all_tweets = bs.find_all('div', {'class':'tweet'})

if all_tweets:
    with open('tweets.csv', 'w', newline='') as csvfile:
        fields = ['author', 'message']
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        
        for tweet in all_tweets[:10]:
            content = tweet.find('div',{'class':'content'})
            header = content.find('div',{'class':'stream-item-header'})
            user = header.find('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
            message_raw = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
            message = re.sub(r'https?:\/\/.*[\r\n]*', '', message_raw, flags=re.MULTILINE)
            
            writer.writerow({'author': handle, 'message': message})