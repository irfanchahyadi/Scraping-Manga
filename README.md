# Scraping-Manga
Scrape manga with python + BeautifulSoup with nice looking web gui

<p align="center">
  <img src="demo/demo.gif"><br/>
  <i>Scraping-Manga</i>
</p>

## Setting Environment (optional)
Ignore this step if you dont want to use virtual environment
```
pip install virtualenv
cd Scraping-Manga
virtualenv venv
venv\Scripts\activate
```

## Requirements
Install required tools
```
pip install -r requirements.txt
```
**This tools require :**
- [Requests](https://github.com/psf/requests), for sending HTTP request to manga web
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup), for parse structure of html 
- [Flask](https://github.com/pallets/flask), for building web gui

## Run program
```
python main.py
```
or run `main.py` file on your favorite IDE, web gui will immidiately show.
Your downloaded manga will saved on Result folder
You can also add new manga with Add Manga menu if you know the link and selector.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzM4NTc0NTIzXX0=
-->