from __main__ import *

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

import sqlite3

def SastoDealScraper(product_keyword):

	conn = sqlite3.connect('test.db')
	cur = conn.cursor()

	cur.execute('''CREATE TABLE IF NOT EXISTS sastodeal
	(
	link_SD CHAR(255) NOT NULL, 
	name_SD CHAR(255) PRIMARY KEY,
	price_SD REAL,
	image_SD CHAR(255),
	parameter_SD CHAR(255)
	)''')
	cur.execute('DELETE FROM sastodeal')

	key= product_keyword.split()
	lenkey= len(key)
	added=key[0];
	for i in range(1,lenkey):
		added= added+'+'+key[i]
	

	print('SASTODEAL\n\n\n')
	my_url = 'https://www.sastodeal.com/sastodeal/faces/search.jsp?searchkey=' + added #changed the pattern

	#opening up connection,grabbing the page
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	# html passing
	page_soup = soup(page_html, "html.parser")

	#changed xpaths

	containers = page_soup.findAll("section",{"class":"categoryProduct category-product categorytDetailDiv "})
  
	for container in containers:

		image_SD = container.a.img["src"]
		link_SD = 'http://www.sastodeal.com'+container.div.a["href"]
		price_SD = container.span.text.replace('?','Rs.')
		title_container =  title_container = container.findAll('a',{"class":'title'})
		name_SD = title_container[0].text.strip()
		parameter_SD= re.split(r'[^\w]',name_SD, re.I| re.M)
		parameter_SD= ''.join(parameter_SD)
		parameter_SD= str.lower(parameter_SD)
		parameter_SD= re.split(r'[^\w]',parameter_SD, re.I| re.M)
		parameter_SD= ''.join(parameter_SD)


		cur.execute("""INSERT OR IGNORE INTO sastodeal(link_SD,name_SD,price_SD,image_SD,parameter_SD)
		VALUES(?,?,?,?,?)""",[link_SD,name_SD,price_SD,image_SD,parameter_SD]);
		conn.commit()
		print("records added")
	containers = page_soup.findAll("section",{"class":"categoryProduct category-product categorytDetailDiv rightbox  "})
  
	for container in containers:

		image_SD = container.a.img["src"]
		link_SD = 'http://www.sastodeal.com'+container.div.a["href"]
		price_SD = container.span.text.replace('?','Rs.')
		title_container =  title_container = container.findAll('a',{"class":'title'})
		name_SD = title_container[0].text.strip()
		a= name_SD
		parameter_SD=re.sub(r'\(.+?\)\a*', '', a)
		parameter_SD= re.split(r'[^\w]',parameter_SD, re.I| re.M)
		parameter_SD= ''.join(parameter_SD)
		parameter_SD= str.lower(parameter_SD)
		parameter_SD= re.split(r'[^\w]',parameter_SD, re.I| re.M)
		parameter_SD= ''.join(parameter_SD)


		cur.execute("""INSERT OR IGNORE INTO sastodeal(link_SD,name_SD,price_SD,image_SD,parameter_SD)
		VALUES(?,?,?,?,?)""",[link_SD,name_SD,price_SD,image_SD,parameter_SD]);
		conn.commit()
		print("records added")
	conn.close()
			 
#SastoDealScraper("Earphones")