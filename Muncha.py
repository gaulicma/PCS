import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import sqlite3
from __main__ import *
from bs4 import BeautifulSoup as soup
import urllib.request

def MunchaDynamicScraper(product_keyword):
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


	class Client(QWebPage):

		def __init__(self,url):
			self.app = QApplication(sys.argv)
			QWebPage.__init__(self)
			self.loadFinished.connect(self.on_page_load)
			self.mainFrame().load(QUrl(url))
			self.app.exec_()
		def on_page_load(self):
			self.app.quit()

	url = "https://muncha.com.np/Product/Search?CategoryID=0&SearchKeyword='"+added+"#"
	client_response = Client(url)
	source = client_response.mainFrame().toHtml()

	page_soup = soup(source, 'html.parser')

	containers = page_soup.findAll("div", class_ = "col-xs-6 col-md-3 ng-scope")

	for container in containers:
		name = container.h5.text
		price = container.span.text
		link = 'https://www.muncha.com' + container.a["href"]
		image = container.img["src"]

		cur.execute("""INSERT OR IGNORE INTO muncha(link, name, price, image)
		VALUES(?,?,?,?)""", [link, name, price, image]);
				
		conn.commit()
		print ("records added")

		#print(name)
		#print(price)
		#print(link)
		#print(image)
	conn.close()

#MunchaDynamicScraper('Samsung')
