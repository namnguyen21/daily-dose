import requests
from bs4 import BeautifulSoup
from pprint import pprint


class NPR_Scraper():
    def __init__(self):
        self.url = 'https://npr.org'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.result = []  # end product will be list of dicts

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

