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
#from sastodeal import SastoDealScraper

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')


#@app.route('/search/<string>')
#def search():
	#return render_template('search.html', details = Details)

@app.route('/search', methods = ['POST','GET'])
def search():
	
	product_keyword = request.form['Product']
	print(product_keyword)
	#KaymuScraper(product_keyword)
	MunchaScraper(product_keyword)
	#SastoDealScraper(product_keyword)
	con = sqlite3.connect("test.db")
	con.row_factory = sqlite3.Row

	cur = con.cursor()
	cur.execute("select * from muncha")

	rows = cur.fetchall();

	return render_template('search.html', rows = rows)
	
if __name__ =='__main__':
	app.run(debug=True)
