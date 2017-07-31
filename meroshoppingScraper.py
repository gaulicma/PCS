
from __main__ import *

import sqlite3
import re

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def MeroShoppingScraper(product_keyword):

	conn = sqlite3.connect('test.db')
	cur = conn.cursor()
	

	cur.execute('''CREATE TABLE IF NOT EXISTS meroshopping(
		link_MS CHAR(255) NOT NULL,
		name_MS CHAR(255) PRIMARY KEY,
		price_MS REAL,
		image_Ms CHAR(255),
		parameter_MS CHAR(255)
		)''')
	cur.execute('DELETE FROM meroshopping')


	print('mero shoping \n\n\n')

	key = product_keyword.split()
	lenkey = len(key)
	added = key[0]
	for i in range(1,lenkey):
		added = added+'+'+key[i]

	my_url = 'https://www.meroshopping.com/search/'+ added
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	page_soup = soup(page_html,'html.parser')
	containers = page_soup.findAll('div',{'class':'col-xs-6 col-md-4 col-lg-3 filtr-item'})

	for container in containers:
		name_MS = container.div.div.text.strip()
		link_MS = 'https://www.meroshopping.com/'+container.a["href"]
		price_container = container.findAll('div',{'class':'price'})
		price_MS = price_container[0].text.strip().replace('NPR','RS.')
		image_MS = 'http://www.meroshopping.com/'+container.img["src"]
		parameter_MS= re.split(r'[^\w]',name_MS, re.I| re.M)
		parameter_MS= ''.join(parameter_MS)
		parameter_MS= str.lower(parameter_MS)
		parameter_MS= re.split(r'[^\w]',parameter_MS, re.I| re.M)
		parameter_MS= ''.join(parameter_MS)



		cur.execute("""INSERT OR IGNORE INTO meroshopping(link_MS,name_MS,price_MS,image_MS,parameter_MS)
		VALUES(?,?,?,?,?)""",[link_MS,name_MS,price_MS,image_MS,parameter_MS]);
		conn.commit()
		print("records added")
	conn.close()


