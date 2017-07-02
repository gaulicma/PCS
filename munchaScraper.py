
from __main__ import *
import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import sqlite3
conn = sqlite3.connect('test.db')
cur = conn.cursor()

#created the table once and then commented it out


#conn.execute('''CREATE TABLE PRODUCT_DETAILS
#			(
#			LINK CHAR(255) NOT NULL,
#			NAME CHAR(255),
#			PRICE REAL,
#			IMG_SRC CHAR(255));''')




def MunchaScraper(product_keyword):
	#product_keyword = input ('what do you want to search')
	#conn.open()
	print('MUNCHA \n\n\n')
	#grab the url
	my_url = 'http://www.shop.muncha.com/Search.aspx?MID=1&q=' + product_keyword

	uClient = uReq(my_url)
	page_html= uClient.read()
	uClient.close()


	#parse the html of the page
	page_soup = soup(page_html,"html.parser")

	#finds all the lines with class as panel panel-default
	containers = page_soup.findAll("div",{"class":"panel panel-default"})
	 

	'''filename = 'muncha.csv'
	f = open(filename, 'w')
	headers =  'link, product_name, prooduct_price \n'
	#f.write(headers)'''


	#grabs individual product
	for contain in containers:
		
		 link = contain.a['href']
		 img_src = contain.img['src']

		 name = contain.div.a.img['alt']
		 
		 price_container = contain.findAll("div",{"class":"price-desc"})
		 price = price_container[0].text.strip()

		 cur.execute("""INSERT INTO PRODUCT_DETAILS(LINK, NAME, PRICE , IMG_SRC)\
		 	VALUES(?,?,?,? )""", [link, name, price, img_src]);
		 print('link '+ link + '\n')
		 print('image ' + img_src+ '\n')
		 print('name '+ name+ '\n')
		 print('price ' + price+ '\n')
		 conn.commit()
		 print ("records added")
		 #conn.close() 
		 #f.write(link +',' + name.replace(',','| ') +',' +  price.replace(',',' ') + '\n')
	conn.close()
MunchaScraper("earphones")