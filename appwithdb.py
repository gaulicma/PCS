from flask import Flask, render_template, url_for 
import os, csv, json
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

#import sqlite3
import sqlite3

#import mySQL 

from kaymuscraper import KaymuScraper

app = Flask(__name__)

def get_connection():
	return sqlite3.connect('db.sqlite3')

def init_db():
	db_conn = get_connection()
	cur = db_conn.cursor()
	_sql = '''SELECT name FROM sqlite_master
	WHERE type = 'table' AND name = 'prod_details'
	'''
	cur.execute(_sql)
	if not cur.fetchone():
		_create_sql = '''CREATE TABLE prod_details(
		website text NOT NULL,
		product_name text NULL,
		product_price REAL NULL,
		link  text NOT NULL, 
		)
	'''
	cur.execute(_create_sql)
	db_conn.commit()


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

@app.route('/search')
def search():
	KaymuScraper()
	return render_template('search.html')
	

if __name__ =='__main__':
	init_db()
	app.run(debug=True)
