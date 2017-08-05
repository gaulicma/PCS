# nepbay scraper

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

from __main__ import *
import sqlite3


def BhatbhateniScraper(product_keyword):


	conn = sqlite3.connect('test.db')
	cur = conn.cursor()
	

	cur.execute('''CREATE TABLE IF NOT EXISTS bhatbhateni(
		link_BB CHAR(255) NOT NULL,
		name_BB CHAR(255) PRIMARY KEY,
		price_BB REAL,
		image_BB CHAR(255),
		p_BB CHAR(255)
		)''')
	cur.execute('DELETE FROM bhatbhateni')


	print('bhatbhateni \n\n\n')

	key = product_keyword.split()
	lenkey = len(key)
	added = key[0]
	for i in range(1,lenkey):
		added = added+'+'+key[i]

	my_url='http://www.bhatbhatenionline.com/search?controller=search&orderby=position&orderway=desc&_qc=0&_qct=All+Categories&search_query='+added+'&submit_search='

	#opening up connection, grab the pageconta
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	#html parser
	page_soup = soup(page_html,"html.parser")

	#grabs each product
	containers = page_soup.findAll("div",{"class":"product-container"})

	for container in containers:
		name_BB = container.h5.text.strip()
		price_BB = container.div.div.div.text.strip()
		image_BB = container.img["src"]
		link_BB = container.a["href"]

		a= name_BB
		p_BB=re.sub(r'\(.+?\)\a*', '', a)
		

		p_BB= re.split(r'[^\w]',p_BB, re.I| re.M)
		p_BB= ''.join(p_BB)
		p_BB= str.lower(p_BB)
		p_BB= re.split(r'[^\w]',p_BB, re.I| re.M)
		p_BB= ''.join(p_BB)


		cur.execute("""INSERT OR IGNORE INTO bhatbhateni(link_BB,name_BB,price_BB,image_BB,p_BB)
		VALUES(?,?,?,?,?)""",[link_BB,name_BB,price_BB,image_BB,p_BB]);
		conn.commit()
		print("records added")
	conn.close()

