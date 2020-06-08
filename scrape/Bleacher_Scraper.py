import requests
from bs4 import BeautifulSoup
from pprint import pprint


class Bleacher_Scraper():
    def __init__(self):
        self.url = 'https://bleacherreport.com/featured'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.result = []  # end product will be list of dicts

    def get_articles(self):
        self.articles = self.soup.find_all(
            'li', {'class': 'cell'})
        pprint(len(self.articles))
        for i in range(15): # get first 15
            title = self.articles[i].find('h3').getText()
            url = self.articles[i].find('a')['href']
            img = self.articles[i].find('img')['src']
            # have to manually change dimension of picture
            large_image = img.replace('h=40&w=60&q=70', 'h=400&w=600&q=70')
            self.result.append({'title': title, 'url': url, 'image': large_image})
        return self.result