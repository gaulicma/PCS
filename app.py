from flask import Flask, render_template, url_for, request, redirect 
import os, csv, json
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import sqlite3
import re

<<<<<<< HEAD




=======
#from kaymuscraper import KaymuScraper
from munchaScraper import MunchaScraper
>>>>>>> aea7c186032fbd6d513bac2c34bce89ba07b4a5a
from sastodeal import SastoDealScraper
from nepbayScraper import NepbayScraper
<<<<<<< HEAD
#from meroshoppingScraper import MeroShoppingScraper
=======
#from meroshopping import MeroShoppingDynamicScraper
>>>>>>> de4c27a94385a189442c237cddcf464f83f355c6
from Muncha import MunchaDynamicScraper
from bhatbhateni import BhatbhateniScraper


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/home.html')
def home():
	return render_template('home.html')


@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/contact.html')
def contact():
	return render_template('contact.html')

@app.route('/another.html', methods=['POST', 'GET'])
def another():
	
	if request.method == "POST":
		c_name = request.form['contacter_name']
		c_email = request.form['contacter_email']
		c_message=request.form['contacter_message']

		conn = sqlite3.connect("test.db")
		curr= conn.cursor()
		curr.execute('''CREATE TABLE IF NOT EXISTS contacter
		(
		name CHAR(255) NOT NULL, 
		email CHAR(255) NOT NULL,
		message CHAR(255) NOT NULL
		)''')
		if c_name:
			curr.execute('''INSERT INTO contacter(name,email,message)
				VALUES(?,?,?)''', [c_name,c_email,c_message]);
			conn.commit()
			return redirect(url_for('thanks'))
	return render_template('another.html')
			
@app.route('/thanks')
def thanks():
	return render_template('thanks.html')

@app.route('/search', methods = ['POST','GET'])
def search():
	
	product_keyword = request.form['Product']
	print(product_keyword)
	#KaymuScraper(product_keyword)
<<<<<<< HEAD

	MunchaDynamicScraper(product_keyword)
=======
<<<<<<< HEAD
<<<<<<< HEAD
#<<<<<<< HEAD
	MunchaDynamicScraper(product_keyword)
=======
<<<<<<< HEAD
	MunchaScraper(product_keyword)
>>>>>>> shradhaN-master
	NepbayScraper(product_keyword)
	SastoDealScraper(product_keyword)
	#MeroShoppingDynamicScraper(product_keyword)
#=======
=======

>>>>>>> aea7c186032fbd6d513bac2c34bce89ba07b4a5a
	#MunchaDynamicScraper(product_keyword)
	#NepbayScraper(product_keyword)
	#SastoDealScraper(product_keyword)
	#MeroShoppingScraper(product_keyword)
<<<<<<< HEAD
<<<<<<< HEAD
#>>>>>>> 219e96c2ce46f61543bbbfb758ec20baf994ef74
=======
>>>>>>> 219e96c2ce46f61543bbbfb758ec20baf994ef74
>>>>>>> shradhaN-master
=======
>>>>>>> de4c27a94385a189442c237cddcf464f83f355c6
	
	#MunchaScraper(product_keyword)
	NepbayScraper(product_keyword)
	SastoDealScraper(product_keyword)
	#MeroShoppingScraper(product_keyword)

<<<<<<< HEAD
	BhatbhateniScraper(product_keyword)
=======
>>>>>>> aea7c186032fbd6d513bac2c34bce89ba07b4a5a
	
>>>>>>> de4c27a94385a189442c237cddcf464f83f355c6

	#make the comparison algorithm here
	conn = sqlite3.connect("test.db")
	
	conn.row_factory = sqlite3.Row

	cur = conn.cursor()
	cur.execute("select * from muncha")

	rows = cur.fetchall();

	cur.execute("select *from NepBay")

	rowsNB = cur.fetchall();
	cur.execute("select * from sastodeal")
	rowsSD = cur.fetchall();

<<<<<<< HEAD
	cur.execute("select * from bhatbhateni")
	rowsBB = cur.fetchall();
	return render_template('search.html', rows = rows, rowsNB = rowsNB, rowsSD = rowsSD, rowsBB = rowsBB)
=======
	#cur.execute("select * from meroshopping")
	#rowsMS = cur.fetchall();
	return render_template('search.html', rows = rows, rowsNB = rowsNB, rowsSD = rowsSD)
>>>>>>> de4c27a94385a189442c237cddcf464f83f355c6


@app.route('/compare', methods = ['POST','GET'])
def compare():
	conn  = sqlite3.connect("test.db")
	conn.row_factory = sqlite3.Row
	cur = conn.cursor()

	cur.execute('''select * from muncha natural join NepBay 
	where muncha.name = NepBay.name_NB''')

	rows = cur.fetchall();

	return render_template('compare.html', rows = rows)




if __name__ =='__main__':

	app.run(debug=True)
