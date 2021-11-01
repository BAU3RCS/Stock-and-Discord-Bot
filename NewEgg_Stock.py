#Brandon Bauer
#26-XX /9/2020
#Loads site, narrows data and finds stock

import time
from bs4 import BeautifulSoup as bs
from Web_Scraping import Client

def getstock(client_response,url):
    print('checkstock1')
    time.sleep(1)
    print('checkstock2')
    source = client_response.get_html(url)
    soup = bs(source,'lxml')
    tag = soup.select('#landingpage-stock')[0]
    stock = tag.select('span')[0].text
    print('checkstock3')
    return stock
