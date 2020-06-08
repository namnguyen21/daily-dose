import requests
from bs4 import BeautifulSoup
from pprint import pprint


class NYT_Scraper():
    def __init__(self):
        self.url = 'https://www.nytimes.com/'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.result = []  # end product will be list of dicts

    def get_articles(self):
        # this will provide hundreds of articles
        self.articles = self.soup.find_all('article')
        # articles have .info.title, a tag, .info.content

        for i in range(15):  # get first 15 articles
            headline = self.articles[i].find('h2')
            if headline is not None: 
                title = headline.getText()
                link = self.articles[i].find('a')['href']
                url = f'https://nytimes.com{link}'
                self.result.append({'title': title, 'url': url})
        return self.result

NYT_Scraper().get_articles()

