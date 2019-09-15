
"""
List manga available
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-Manga
"""

import csv

def get(id):
    with open('crawler/manga_list.csv', 'r') as f:
        for row in csv.reader(f):
            if row[0] == id:
                return row