
from __main__ import *
import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import sqlite3





def MunchaScraper(product_keyword):

	conn = sqlite3.connect('test.db')
	
	cur = conn.cursor()
	#created the table once and then commented it out
	cur.execute('''CREATE TABLE IF NOT EXISTS muncha
	(
	link CHAR(255) NOT NULL, 
	name CHAR(255) PRIMARY KEY,
	price REAL,
	image CHAR(255)
	)''')
	cur.execute('DELETE FROM muncha')


	#product_keyword = input ('what do you want to search')
	#conn.open()
	print('MUNCHA \n\n\n')

	
	key= product_keyword.split()
	lenkey= len(key)
	added=key[0];
	for i in range(1,lenkey):
		added= added+'+'+key[i]
	
	
	
	my_url = 'https://muncha.com.np/Product/Search?CategoryID=0&SearchKeyword='+added


	uClient = uReq(my_url)
	page_html= uClient.read()
	uClient.close()


	#parse the html of the page
	page_soup = soup(page_html,"html.parser")

	#finds all the lines with class as panel panel-default
	containers = page_soup.findAll("div",{"class":"col-xs-6 col-md-3 ng-scope"})
	 

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
		 price = price_container[0].text.strip()# why is this here
		 try:
		 	present, past = price.split()
		 except:
		 	present = price


		 s_name = name.replace('-',' ')
		 r = s.split()
		 for i in r:
		 	if i==product_keyword:			
				 cur.execute("""INSERT OR IGNORE INTO muncha(link, name, price, image)
				 VALUES(?,?,?,?)""", [link, s_name, present, img_src]);
				 '''print('link '+ link + '\n')
				 print('image ' + img_src+ '\n')
				 print('name '+ name+ '\n')
				 print('price ' + present+ '\n')'''
				 conn.commit()
				 print ("records added")
		 #conn.close() 
		 #f.write(link +',' + name.replace(',','| ') +',' +  price.replace(',',' ') + '\n')
	conn.close()# use this for the last website
#MunchaScraper("Samsung")