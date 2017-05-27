from flask import Flask, render_template, url_for 
import os, csv, json
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re



from kaymuscraper import KaymuScraper

app = Flask(__name__)



@app.route('/')
def index():
	#ReadAsin()
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
	app.run(debug=True)
