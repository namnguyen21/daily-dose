import requests
from bs4 import BeautifulSoup
from pprint import pprint


class Usa_Scraper():
    def __init__(self):
        self.url = 'https://www.usatoday.com/news'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.result = []  # end product will be list of dicts

    def get_articles(self):
        top_stories = self.soup.find('div', {'aria-label': 'More Top Stories'})
        articles = top_stories.find_all('a')
        for article in articles:
            # get all sub elements of articles
            title = article.text
            if len(title) > 1:  # need to account for blank titles
                image = article.find('img')['data-gl-src']
                link = article['href']
                url = f'https://usatoday.com/{link}'
                self.result.append(
                    {'title': title, 'url': url, 'image': image})
        return self.result

