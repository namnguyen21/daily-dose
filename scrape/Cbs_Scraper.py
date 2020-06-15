import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class Cbs_Scraper(Scraper):
    def get_articles(self):
        articles = self.soup.find_all('article')
        for i in range(15): 
            article = articles[i]
            title = article.find('h4').getText()
            href = article.find('a')['href']
            self.result.append({'title': title, 'url': href})
        return self.result