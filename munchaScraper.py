import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


product_keyword = input ('what do you want to search')
#grab the url
my_url = 'http://www.shop.muncha.com/Search.aspx?MID=1&q=' + product_keyword

uClient = uReq(my_url)
page_html= uClient.read()
uClient.close()


#parse the html of the page
page_soup = soup(page_html,"html.parser")

#finds all the lines with class as panel panel-default
containers = page_soup.findAll("div",{"class":"panel panel-default"})
 

filename = 'muncha.csv'
f = open(filename, 'w')
headers =  'link, product_name, prooduct_price \n'
#f.write(headers)


#grabs individual product
for contain in containers:
	 link = contain.a['href']

	 name = contain.div.a.img['alt']
	 
	 price_container = contain.findAll("div",{"class":"price-desc"})
	 price = price_container[0].text.strip()


	 print('link '+ link)
	 print('name '+ name)
	 print('price ' + price)
 
	 f.write(link +',' + name.replace(',','| ') +',' +  price.replace(',',' ') + '\n')
f.close()