
"""
Main file
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-Manga
"""

import os

crawl_status = 0			# 0: Idle, 1: Crawling, 2: Stopped
crawl_manga = '-'
crawl_now = 0
crawl_end = 0

directory = os.path.join(os.getcwd(), 'Result')
if not os.path.isdir(directory):
    os.mkdir(directory)

from gui import web