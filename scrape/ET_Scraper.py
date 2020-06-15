import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class ET_Scraper(Scraper):
    def get_articles(self):
        articles = self.soup.find_all('article')
        for article in articles: 
            h2 = article.find('h2')
            a = h2.find('a')
            title = a.getText()
            href = a['href']
            url = f'https://etonline.com{href}'
            self.result.append({'title': title, 'url': url})
        return self.result
