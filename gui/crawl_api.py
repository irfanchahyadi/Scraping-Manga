
"""
API for crawl worker
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-Manga
"""

import sys

from threading import Thread
sys.path.append('Scraping-Manga')
from crawler import manga_list
from crawler import mangaku

def get(id):
    id, name, engine, url = manga_list.get(id)
    
    if engine == 'mangaku':
        engine = mangaku.Crawl
        
    t = Thread(target=engine, args=(name, url))
    t.start()