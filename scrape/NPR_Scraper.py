import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class NPR_Scraper(Scraper):
    def get_articles(self):
        articles = self.soup.find_all('div', {'class': 'story-wrap'})
        for article in articles:
            image = article.find('img')
            # we only want ones with images
            if image is not None:
                src = image['src']
                title = article.find('h3').getText()
                url = article.find('a')['href']
                self.result.append({'title': title, 'image': src, 'url': url})
            else:
                continue
        return self.result
