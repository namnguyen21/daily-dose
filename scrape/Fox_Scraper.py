import requests
from bs4 import BeautifulSoup
from Scraper import Scraper


class Fox_Scraper(Scraper):
    def get_articles(self):
        # this will provide hundreds of articles
        self.articles = self.soup.find_all('article')
        # articles have .info.title, a tag, .info.content

        for i in range(15):  # get first 15 articles
            htmlatag = self.articles[i].find("h2", class_="title").find("a")
            title = htmlatag.getText()
            url = htmlatag.get("href")
            d = {"title": title, "url": url}
            self.result.append(d)
        return self.result

