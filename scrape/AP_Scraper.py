import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class AP_Scraper(Scraper):
    def get_articles(self):
        articles = self.soup.find_all('div', {'class': 'RelatedStory'})
        for article in articles: 
            a = article.find('a')
            href = a['href']
            title = article.find('div').getText()
            url = f'https://apnews.com{href}'
            self.result.append({'title': title, 'url': url})
        return self.result