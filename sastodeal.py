from __main__ import *

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def SastoDealScraper(product_keyword):

	print('SASTODEAL\n\n\n')
	my_url = 'https://www.sastodeal.com/search?q=' + product_keyword + '&SearchSastodeal=Search'

	#opening up connection,grabbing the page
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	# html passing
	page_soup = soup(page_html, "html.parser")

	filename = 'sasto.csv'
	f=open(filename, 'w')
	headers = 'product_name , price , link\n'
	f.write(headers)


	containers = page_soup.findAll("div",{"class":"pure-u-1-3 product_box item_box size-hover"})

	for contain in containers:
		title_contain = contain.findAll("div", {"class":"one_product_title"})
		name = title_contain[0].text.strip()
		title_contain[0].text.strip()


		price = contain.span.text

		link = contain.a['href']

		
		print("product_name:" + name)
		print("price" + price)
		print("link" + link)

		f.write(name.replace(',' , '')+',' + price.replace(',' , '')+ ',' + link+ '\n')
	f.close()
	 
