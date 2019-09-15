
"""
Scraping Manga from komikid.com
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-komikid
"""

# IMPORT REQUIRED PACKAGE
import os, requests, bs4

# GET LIST OF ALL CHAPTER
def get_all_chapter():
    res = requests.get('http://www.komikid.com/manga/one-piece')
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    chapters = soup.select('h5.chapter-title-rtl > a')
    chapters = [(c['href'], c.get_text()) for c in chapters]
    for h, t in chapters:
        download(h, t)

# DOWNLOAD EACH CHAPTER
def download(html, text):
    res = requests.get(html)
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    pages = soup.select('#all > img')
    
    # Create Chapter folder
    folder_dir = os.path.join(directory, text)
    if not os.path.isdir(folder_dir):
        os.mkdir(folder_dir)
    
    # Download each Page
    for i, p in enumerate(pages):
        href =  p['data-src'].strip()
        filename = os.path.join(folder_dir, str(i+1) + href[-4:])
        if not os.path.isfile(filename):
            print('downloading {} page {}'.format(text, i+1))
            try:
                img = requests.get(href)
                with open(filename, 'wb') as f:
                    for chunk in img.iter_content(100000):
                        f.write(chunk)
            except Exception as e:
                print('{} at {} page {}'.format(e, text, i+1))
        else:
            print('already have {} page {}'.format(text, i+1))

if __name__ == '__main__':
    directory = os.path.join(os.getcwd(), 'One Piece')
    
    # Create Manga folder if not exists
    if not os.path.isdir(directory):
        os.mkdir(directory)
        
    get_all_chapter()