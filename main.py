
"""
Main file
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-Manga
"""

import os

directory = os.path.join(os.getcwd(), 'Result')
if not os.path.isdir(directory):
    os.mkdir(directory)

from gui import web
