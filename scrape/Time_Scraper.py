import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class Time_Scraper(Scraper):
    def get_articles(self):
        articles = self.soup.find_all('article')
        for i in range(20):
            article = articles[i]
            h2 = article.find('h2')
            a = h2.find('a')
            title = a.getText()
            href = a['href']
            link = f'https://time.com{href}'
            self.result.append({'title': title, 'url': link})
        return self.result
