import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import sqlite3
from __main__ import *
from bs4 import BeautifulSoup as soup
import urllib.request


def MeroShoppingDynamicScraper(product_keyword):

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

	print('Meroshooping')

	key = product_keyword.split()
	lenkey = len(key)
	added = key[0]
	for i in range(1,lenkey):
		added = added+'+'+key[i]


	class Client(QWebPage):
		def __init__(self, url):
			self.app = QApplication(sys.argv)
			QWebPage.__init__(self)
			self.loadFinished.connect(self.on_page_load)
			self.mainFrame().load(QUrl(url))
			self.app.exec_()

		def on_page_load(self):
			self.app.quit()

	

	url = "https://www.meroshopping.com/search/"+ added
	client_response = Client(url)
	source = client_response.mainFrame().toHtml()

	

	page_soup = soup(source,'html.parser')
	containers = page_soup.findAll('div',class_='col-xs-6 col-md-4 col-lg-3 filtr-item')
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






		