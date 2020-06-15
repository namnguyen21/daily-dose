import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class Buzzfeed_Scraper(Scraper):
    def get_articles(self):
        articles = self.soup.find_all('article') # 100+ articles
        for i in range(15):
            article = articles[i]
            url = article.find('a')['href']
            headline = article.find('h2')
            if headline is not None: 
                title = headline.getText()
                self.result.append({'title': title, 'url': url})
        return self.result