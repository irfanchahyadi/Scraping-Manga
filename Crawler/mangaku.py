
"""
Scraping Manga from mangaku.in
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-komikid
"""

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

# IMPORT REQUIRED PACKAGE
import os, requests, bs4, re

# GET LIST OF ALL CHAPTER
def get_all_chapter(sub_url):
    url = 'http://www.mangaku.in/' + sub_url
    usr = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    hdr = {'User-Agent': usr}
    res = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    chapters = soup.select('small')[5].select('a')
    for c in chapters:
        url = c['href']
        chapter = clean_chapter_name(c.get_text())
        
        folder_dir = os.path.join(directory, chapter)
        if not os.path.isdir(folder_dir):
            os.mkdir(folder_dir)
            pages = download(url, chapter)
            print(' '*50, end='\r')
            print('{} downloaded, {} pages.'.format(chapter, pages))

# SAFE CREATE DIRECTORY
def safe_mkdir(text):
    try:
        os.mkdir(text)
    except:
        safe_text = ''
        for c in text:
            if c.isalnum() or c in [' ','.','/']:
                safe_text = safe_text + c
        os.mkdir(safe_text)

# CLEAN CHAPTER NAME
def clean_chapter_name(text):
    regex = re.compile('Chapter\s\d{1,4}[\,\.]?\d{1}')
    result = regex.findall(text)
    result = text if len(result) == 0 else result[0]
    result = result.replace(',', '.')
    new_result = ''
    for c in result.strip():
        if c.isalnum() or c in [' ','.','/']:
            new_result = new_result + c
    return new_result

# DOWNLOAD EACH CHAPTER
def download(url, chapter):
    res = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    pages = soup.select('div.separator > a > img') + soup.select('img.aligncenter')
    
    # Download each Page
    i = 1
    for p in pages:
        href =  p['src'].strip()
        href = 'https:' + href if href[0] != 'h' else href
        file_format = '.png' if href[-4] != '.' else href[-4:]
        filename = os.path.join(directory, chapter, str(i) + file_format)
        if file_format == '.gif':
            continue
        
        if not os.path.isfile(filename):
            print('downloading {} page {}...'.format(chapter, i), end='\r')
            try:
                img = requests.get(href, headers=HEADERS)
                with open(filename, 'wb') as f:
                    for chunk in img.iter_content(1024):
                        f.write(chunk)
            except Exception as e:
                print('{} at {} page {}'.format(e, chapter, i))
        else:
            print('already have {} page {}'.format(chapter, i), end='\r')
        i += 1
    return i - 1

if __name__ == '__main__':
    directory = os.path.join(os.getcwd(), 'One Piece')
    
    # Create Manga folder if not exists
    if not os.path.isdir(directory):
        os.mkdir(directory)
        
    get_all_chapter('baca-komik-one-piece-bahasa-indonesia/')