import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class Nbc_Scraper(Scraper):
    def get_articles(self):
        articles = self.soup.find_all('article')
        for article in articles: 
            a = article.find('a')
            if a is not None: 
                href = a['href']
                title = article.find_all('h2')[1].find('span').getText()
                self.result.append({'title': title, 'url': href})
        return self.result
            