
"""
Web GUI
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-Manga
"""

# IMPORT REQUIRED PACKAGE
from flask import Flask, render_template, request, redirect, url_for, Response
import os, webbrowser, time
from gui import web_api
import main

app = Flask(__name__)

@app.route('/tes')
def tes():
	return render_template('index2.html')

@app.route('/')
def home():
	manga = web_api.get_manga()
	lang = web_api.get_lang()
	return render_template('index.html', data={'manga': manga, 'lang': lang})

@app.route('/crawl/<path:id_lang>')
def crawl(id_lang):
	id, lang_id = id_lang.split('_')
	web_api.get(id, lang_id)
	return redirect(url_for('home'))

@app.route('/stop_crawl')
def stop_crawl():
    web_api.stop()
    return ('', 204)

@app.route('/shutdown')
def shutdown():
	shutdown_server()
	return "Bye, see other project on <a href='https://github.com/irfanchahyadi'>github.com/irfanchahyadi</a>"

def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()

@app.route('/progress')
def progress():
    def generate():
        x = 0
        while x <= 200:
            yield 'data: {"now":' + str(main.crawl_now) + ', "end":' + str(main.crawl_end) + ', "manga":"' + main.crawl_manga + '"}\n\n'
            x = x + 1
            time.sleep(0.5)
    return Response(generate(), mimetype='text/event-stream')

@app.route('/new_manga', methods=['POST'])
def new_manga():
	form = request.form.to_dict()
	imageFile = request.files['imageFile']
	web_api.add_manga(form, imageFile)
	return redirect(url_for('home'))


webbrowser.open_new_tab('http://localhost:5000/')

app.run(host='0.0.0.0')
