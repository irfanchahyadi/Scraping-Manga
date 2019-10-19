
"""
API for crawl worker
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-Manga
"""

import sys, sqlite3, os

from threading import Thread
sys.path.append('Scraping-Manga')
from crawler import mangaku
import main
from werkzeug import secure_filename

con = sqlite3.connect('gui/static/database/manga.db', check_same_thread=False)

def get(id, lang_id):
    id, name, lang_id, engine, sub_url, selectors = get_manga(id, lang_id)
    if engine == 'mangaku':
    	main.crawl_status = 1
    	main.crawl_manga = name
    	engine = mangaku.Crawl
    
    t = Thread(target=engine, args=(name, sub_url, selectors))
    t.start()

def stop():
	main.crawl_status = 2

def get_manga(id=None, lang_id=None):
	cur = con.cursor()
	if id and lang_id:
		command = 'SELECT a.id, a.name, b.lang_id, b.crawler, b.sub_url, b.selectors FROM manga_list a INNER JOIN manga_crawler b ON a.id=b.id WHERE a.id=? AND b.lang_id=?;'
		cur.execute(command, (id, lang_id))
		rows = cur.fetchone()
	elif id:
		cur.execute('SELECT * FROM manga_list WHERE id=?;', (id,))
		rows = cur.fetchone()
	else:
		cur.execute('SELECT * FROM manga_list;')
		rows = cur.fetchall()
	return rows

def get_lang():
	cur = con.cursor()
	cur.execute('SELECT * FROM manga_language;')
	rows = cur.fetchall()
	return rows

def add_manga(form, imageFile):
	mangaName = form['mangaName']
	filename = secure_filename(imageFile.filename)
	filedir = 'gui/static/images/image002.png'
	imageFile.save('gui/static/images/' + filename)
	imageFile = filename
	description = form['description']
	language = form['language']
	crawler = form['crawler']
	url = form['url']
	selector = form['selector']
	cur = con.cursor()
	insert_new_manga_list = "INSERT INTO manga_list (name, image, description) VALUES (?, ?, ?)"
	cur.execute(insert_new_manga_list, (mangaName, imageFile, description))
	con.commit()
	cur.execute('SELECT id FROM manga_list WHERE name=?;', (mangaName,))
	id = cur.fetchone()[0]
	insert_new_manga_crawler = "INSERT INTO manga_crawler (id, lang_id, crawler, sub_url, selectors) VALUES (?, ?, ?, ?, ?)"
	cur.execute(insert_new_manga_crawler, (id, language, crawler, url, selector))
	con.commit()