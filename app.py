from flask import Flask, render_template, url_for 
import os, csv, json

from search import ReadAsin

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

if __name__ =='__main__':
	app.run(debug=True)
