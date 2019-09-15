
"""
Web GUI
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-Manga
"""

# IMPORT REQUIRED PACKAGE
from flask import Flask, render_template
import os, webbrowser
from gui import crawl_api

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/crawl/<path:name>')
def crawl(name):
    crawl_api.get(name)
    return render_template('index.html');

webbrowser.open_new_tab('http://localhost:5000/')
app.run(host='0.0.0.0')