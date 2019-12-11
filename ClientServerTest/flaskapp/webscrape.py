import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline

from urllib.request import urlopen
import bs4
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/2019/12/10/us/politics/trump-impeachment-articles.html?action=click&module=Top%20Stories&pgtype=Homepage"
html = urlopen(url)

textfile = BeautifulSoup(html, 'lxml')
type(textfile)

bs4.BeautifulSoup


title = textfile.title
print(title)

text = textfile.get_text()
print(text)
