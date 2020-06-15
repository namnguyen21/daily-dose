import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class WSJ_Scraper(Scraper):
    def get_articles(self):
        articles = self.soup.find_all('article')
        for article in articles: 
            a = article.find('h2').find('a')
            url = a['href']
            title = a.getText()
            self.result.append({'title': title, 'url': url})
        return self.result