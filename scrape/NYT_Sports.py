import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper

class NYT_Sports(Scraper):
    def get_articles(self):
        section = self.soup.find('section', {'id': 'stream-panel'})
        ol = section.find('ol')  # list of articles
        articles = ol.find_all('li')
        for article in articles:
            title = article.find('h2').getText()
            image = article.find('img')['src']
            url = article.find('a')['href'] 
            self.result.append({'title': title, 'image': image, 'url': url})
        return self.result

