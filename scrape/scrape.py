#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import time
wines=[]
def scrape_all(inputValue):
    #inputValue = input("what is your zipcode? ")
    url ='https://www.totalwine.com/store-finder?q=78613&radius1=200'
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = f'https://www.totalwine.com/store-finder?q={inputValue}&radius1=200'
    browser.visit(url)
    time.sleep(1)
    time.sleep(2)
    browser.click_link_by_id("btnYes")
    time.sleep(4)
    #browser.click_link_by_id('header-search-text')
    browser.click_link_by_id('at_searchProducts')
    html= browser.html
    soup=BeautifulSoup(html, "html.parser")
    search = soup.find_all('a', class_='analyticsStoreLink')
    time.sleep(2)
    wines.append(search[0]['href'])
    browser.fill('text', 'Seven Falls Chardonnay')
    browser.click_link_by_id('at_searchProductsBtn')
    time.sleep(3)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')
    search = soup.find_all('h2', class_='plp-product-title')
    for t in search:
       if(t.a):
          wines.append(t.a['aria-label'])
    print(wines)        
    browser.quit()
    return wines

