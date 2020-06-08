import requests
from bs4 import BeautifulSoup
from pprint import pprint


class Si_Scraper():
    def __init__(self):
        self.url = 'https://www.si.com/'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.result = []  # end product will be list of dicts

    def get_articles(self):
        self.articles = self.soup.find_all(
            'article', {'class': 'm-card'})
        for i in range(15):
            image = self.articles[i].find('img')
            if image is not None: 
                src = image['src']
            else: # default SI logo if no image
                src = 'https://www.afsc.org/sites/default/files/styles/maxsize/public/images/sports%20illustrated.jpg?itok=iqCSSAZw'
            title = self.articles[i].find('h2').getText()
            href = self.articles[i].find('a')['href']
            url = f'https://si.com{href}'
            self.result.append({'title': title, 'url': url, 'image': src})
        return self.result