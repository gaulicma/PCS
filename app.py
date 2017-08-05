from flask import Flask, render_template, url_for, request, redirect 
import os, csv, json
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import sqlite3
import re






from sastodeal import SastoDealScraper
from nepbayScraper import NepbayScraper

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


	#MunchaDynamicScraper(product_keyword)
	#NepbayScraper(product_keyword)
	#SastoDealScraper(product_keyword)
	#BhatbhateniScraper(product_keyword)


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


	cur.execute("select * from bhatbhateni")
	rowsBB = cur.fetchall();
	return render_template('search.html', rows = rows, rowsNB = rowsNB, rowsSD = rowsSD, rowsBB = rowsBB)




@app.route('/compare', methods = ['POST','GET'])
def compare():
	conn  = sqlite3.connect("test.db")
	conn.row_factory = sqlite3.Row
	cur = conn.cursor()

	#cur.execute('''select * from muncha natural join NepBay 
	#where muncha.parameter = NepBay.p_NB''')
	cur.execute("""
		create view if not exists view_table2 as
		select * from NepBay natural join muncha natural join bhatbhateni
 		where
 		NepBay.p_NB = muncha.parameter
 		and NepBay.p_NB = bhatbhateni.p_BB
 		and muncha.parameter = bhatbhateni.p_BB""")
	cur.execute("select * from view_table2")
	rows = cur.fetchall();

	cur.execute("""
		create view if not exists view_table4 as
	select * from NepBay natural join muncha
	where NepBay.p_NB = muncha.parameter""")
	cur.execute("select * from view_table4")
	rows2 = cur.fetchall();
	return render_template('compare.html', rows = rows, rows2 = rows2)
	



if __name__ =='__main__':

	app.run(debug=True)
