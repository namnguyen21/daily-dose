import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class Reuters_Scraper(Scraper):
    def get_articles(self):
        articles = self.soup.find_all('article')
        for i in range(15):
            article = articles[i]
            headline = article.find('h3')
            if headline is not None:
                href = article.find('a')['href']
                title = headline.getText()
                url = f'https://www.reuters.com{href}'
                self.result.append({'title': title, 'url': url})
        return self.result
