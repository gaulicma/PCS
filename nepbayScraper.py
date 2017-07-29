# nepbay scraper

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

from __main__ import *
import sqlite3


def NepbayScraper(product_keyword):


	conn = sqlite3.connect('test.db')
	cur = conn.cursor()
	

	cur.execute('''CREATE TABLE IF NOT EXISTS NepBay(
		link_NB CHAR(255) NOT NULL,
		name_NB CHAR(255) PRIMARY KEY,
		price_NB REAL,
		image_NB CHAR(255)
		)''')
	cur.execute('DELETE FROM NepBay')


	print('NEPBAY \n\n\n')

	key = product_keyword.split()
	lenkey = len(key)
	added = key[0]
	for i in range(1,lenkey):
		added = added+'+'+key[i]

	my_url='https://nepbay.com/shopping/search/auctions/?search%5Bkeyword%5D='+added+'&abstractauction_form_posted=search_auction'

	#opening up connection, grab the pageconta
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	#html parser
	page_soup = soup(page_html,"html.parser")

	#grabs each product
	containers = page_soup.findAll("div",{"class":"item"})

	for container in containers:
		name_NB = container.span.text.strip()
		image_NB = container.a.img["src"]
		link_NB = container.a["href"]
		price_container = container.findAll("div",{"class":"search-price"})
		price_NB = price_container[0].text.strip().replace("रु","Rs")

		cur.execute("""INSERT OR IGNORE INTO NepBay(link_NB,name_NB,price_NB,image_NB)
		VALUES(?,?,?,?)""",[link_NB,name_NB,price_NB,image_NB]);
		conn.commit()
		print("records added")
	conn.close()

#NepbayScraper('earphone')


