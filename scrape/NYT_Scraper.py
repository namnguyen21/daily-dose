import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class NYT_Scraper(Scraper):
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


