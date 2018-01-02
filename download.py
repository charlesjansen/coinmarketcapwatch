
from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote
import urllib
import json
from bs4 import BeautifulSoup
import re
from os.path import isfile, isdir
from tqdm import tqdm
import time
import pickle
import csv
import pandas as pd
from connect import connectAndCheck
from config import webdriverpath
from helper import die


browser = webdriver.Chrome(webdriverpath)
url = r"https://coinmarketcap.com/all/views/all/"
searchTypeString = "body > div.outer-container.global-stats.desktop.hidden-xs > div > div > div.col-sm-6.text-center > ul > li:nth-child(1)"
searchType = "CSS_SELECTOR"

connectAndCheck(url, searchTypeString, browser, searchType)

mainTable = browser.find_element_by_tag_name('tbody')
html = mainTable.get_attribute('innerHTML')#does give me the real compiled code post javascript

soup = BeautifulSoup(html, "lxml")
data =[]
for tr in soup.find_all("tr"):
    #print(tr["id"])
    #print(tr.td"class"])
    cells = tr.find_all("td")
    coinData = []
    coinData.append(cells[0].find(text=True).strip())#rank
    coinData.append(cells[1].find_all("a")[1].find(text=True).strip())#name
    coinData.append(cells[2].find(text=True).strip())#symbol
    coinData.append(cells[3].find(text=True).strip().strip("$").replace(",",""))#market cap
    coinData.append(cells[4].a.find(text=True).strip().strip("$").replace(",",""))#price
    coinData.append(cells[5].find(text=True).strip().strip("$").replace(",",""))#supply
    coinData.append(cells[6].a.find(text=True).strip().strip("$").replace(",",""))#volume
    coinData.append(cells[7].find(text=True).strip())#change 1h
    coinData.append(cells[8].find(text=True).strip())#change 24h
    coinData.append(cells[9].find(text=True).strip())#change 7d
    
    data.append(coinData)

labels = ["rank","name","symbol","market cap","price","supply","volume","change 1h","change 24h","change 7d"]
data = pd.DataFrame.from_records(data, columns=labels)
del labels, html, coinData, searchType, searchTypeString

#Pour excel
pricesExcel = data.loc[data["symbol"].isin(["NEO","XVG","ETH","AE","ADA","VEN","ETN","XRP","CTR","EDG","NULS","DNR","XLM","STORJ","TRX","QTUM","SAFEX"])]

#pour stocker














browser.quit()
















