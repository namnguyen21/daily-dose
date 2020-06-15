import requests
from bs4 import BeautifulSoup
from pprint import pprint
from Scraper import Scraper


class ESPN_Scraper(Scraper):
    def get_articles(self):
        # this will provide hundreds of articles
        self.articles = self.soup.find_all(
            'section', {'class': 'contentItem__content'})
        for i, article in enumerate(self.articles):
            try: 
                image = article.find('img')
                if image.has_attr('src'):
                    src = image['src']
                elif image.has_attr('data-default-src'): 
                    src = image['data-default-src']
                else: # default espn logo if no image source
                    src = 'https://dunkelite.com/wp-content/uploads/2016/03/ESPN-logo.png'
            except KeyError as err: 
                print(err)
            headline = article.find('h1', {'class': 'contentItem__title'})
            if headline is not None: 
                title = headline.getText()
                link = article.find('a')
                if link is not None: # certain articles wont have linkes
                    href = link['href']
                    url = f'https://espn.com{href}'
                else : 
                    url = 'https://espn.com' # use base espn url in case no link
                self.result.append({'title': title, 'url': url, 'image': src})
        return self.result