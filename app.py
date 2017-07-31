from flask import Flask, render_template, url_for, request, redirect 
import os, csv, json
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import sqlite3


#import mySQL 
#



#from kaymuscraper import KaymuScraper
from munchaScraper import MunchaScraper
from sastodeal import SastoDealScraper
from nepbayScraper import NepbayScraper
from meroshoppingScraper import MeroShoppingScraper


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
	MunchaScraper(product_keyword)
	NepbayScraper(product_keyword)
	SastoDealScraper(product_keyword)
	MeroShoppingScraper(product_keyword)
	

	#make the comparison algorithm here
	con = sqlite3.connect("test.db")
	con.row_factory = sqlite3.Row

	cur = con.cursor()
	cur.execute("select * from muncha")

	rows = cur.fetchall();

	cur.execute("select *from NepBay")

	rowsNB = cur.fetchall();
	cur.execute("select * from sastodeal")
	rowsSD = cur.fetchall();

	cur.execute("select * from meroshopping")
	rowsMS = cur.fetchall();
	return render_template('search.html', rows = rows, rowsNB = rowsNB, rowsSD = rowsSD, rowsMS = rowsMS)

	#do for mero shopping

'''@app.route('/message', methods = ['GET','POST'])
def message():
	if request.method == 'POST':
		conn = sqlite3.connect('test.db')
		cur = conn.cursor()
		#cur.execute(CREATE TABLE IF NOT EXISTS message(
		name CHAR(50),
		email CHAR(255),
		message CHAR(255)
		)
		name = request.form['contacter_name'] 
		email = request.form['contacter_email']
		message = request.form['contacter_message']

		if name():
			cur.execute(INSERT INTO message(name,emai,message)
				VALUES(?,?,?), [name,email,message]);
			cur.commit()
			return redirect(url_for('thank.html'))
	return render_template('another.html')

'''


	
if __name__ =='__main__':
	app.run(debug=True)
