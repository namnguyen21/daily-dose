import requests
from bs4 import BeautifulSoup


class Scraper():
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.result = []  # end product will be list of dicts
