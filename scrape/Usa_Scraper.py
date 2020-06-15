import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper

class Usa_Scraper(Scraper):
    def get_articles(self):
        top_stories = self.soup.find('div', {'aria-label': 'More Top Stories'})
        articles = top_stories.find_all('a')
        for article in articles:
            # get all sub elements of articles
            title = article.text
            if len(title) > 1:  # need to account for blank titles
                image = article.find('img')#['data-gl-src']
                if image is not None: 
                    src = image['data-gl-src']
                    link = article['href']
                    url = f'https://usatoday.com/{link}'
                    self.result.append(
                        {'title': title, 'url': url, 'image': src})
        return self.result
