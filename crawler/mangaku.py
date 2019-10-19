
"""
Scraping Manga from mangaku.in
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-Manga
"""

# IMPORT REQUIRED PACKAGE
import os, requests, bs4, re
import main

# FIX CONSTANT
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

class Crawl():
    # INIT
    def __init__(self, name, sub_url, selectors):
        self.directory = os.path.join(os.getcwd(), 'Result', name)
        # Create Manga folder if not exists
        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)
        self.get_all_chapter(sub_url, selectors)

    # GET LIST OF ALL CHAPTER
    def get_all_chapter(self, sub_url, selectors):
        url = 'http://www.mangaku.in/' + sub_url
        res = requests.get(url, headers=HEADERS)
        soup = bs4.BeautifulSoup(res.content, 'html.parser')
        chapters = []
        for selector in selectors.split(';')[::-1]:
            temp = soup.select(selector)[::-1]
            chapters = chapters + temp
        num_chapters = len(chapters)
        main.crawl_end = num_chapters
        print(num_chapters)

        for idx, c in enumerate(chapters):
            url = c['href']
            chapter = self.clean_chapter_name(c.get_text())

            folder_dir = os.path.join(self.directory, chapter)
            if not os.path.isdir(folder_dir):
                os.mkdir(folder_dir)
            pages = self.download(url, chapter)
            print(' '*50, end='\r')
            if main.crawl_status == 2:
                print('crawling stopped')
                break
            else:
                print('{} downloaded, {} pages.'.format(chapter, pages))
                main.crawl_now = idx + 1
                main.crawl_end = num_chapters

        if main.crawl_status == 1:
            main.crawl_status = 0
            print('All chapters downloaded')

    # CLEAN CHAPTER NAME
    def clean_chapter_name(self, text):
        regex = re.compile('Chapter\s\d{1,4}[\,\.]?\d{0,1}')
        result = regex.findall(text)
        result = text if len(result) == 0 else result[0]
        result = result.replace(',', '.')
        new_result = ''
        for c in result.strip():
            if c.isalnum() or c in [' ','.','/']:
                new_result = new_result + c
        return new_result

    # DOWNLOAD EACH CHAPTER
    def download(self, url, chapter):
        res = requests.get(url, headers=HEADERS)
        soup = bs4.BeautifulSoup(res.content, 'html.parser')
        pages = soup.select('div.separator > a > img') + soup.select('img.aligncenter')
        
        # Download each Page
        i = 1
        for p in pages:
            href =  p['src'].strip()
            href = 'https:' + href if href[0] != 'h' else href
            file_format = '.png' if href[-4] != '.' else href[-4:]
            filename = os.path.join(self.directory, chapter, str(i) + file_format)
            if main.crawl_status == 2:
                break

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