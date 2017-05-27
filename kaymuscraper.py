import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re


def KaymuScraper():
	product_keyword = input('enter the name of the product')
	my_url = 'http://www.kaymu.com.np/catalog/?q='+product_keyword
	# opening up connection and grabbing The page
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()#closes the client

	page_soup = soup(page_html,"html.parser")# parse the page

	containeres = page_soup.findAll("div",{"class":"small-3 productItem no-shrink mvs"})# grabs content inside div class small-3 productItem..

	filename ='Products.csv'
	f = open(filename,"w")
	headers = "Name, Price \n"
	for container in containeres:

		name = container.a.div.img["alt"]
	
		price_container = container.section.findAll("div", {"class":"prices"})
		product_price = price_container[0].text


		link = container.a["href"]
	

		print("Name " + name)
		print("Product Price"+ product_price)
		print("link" + link)



		f.write(name.replace(","," ") + "," + product_price.replace(",","") + "," + "http://www.kaymu.com.np/" + link + "\n")
	f.close()