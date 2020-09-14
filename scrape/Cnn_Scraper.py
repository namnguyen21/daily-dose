from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
from pprint import pprint


class Cnn_Scraper():
    def __init__(self):
        self.result = []
        url = "https://www.cnn.com/"
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.get(url)
        sleep(5)

    def get_articles(self):
        page = self.driver.page_source
        self.driver.quit()
        soup = BeautifulSoup(page, 'html.parser')
        # must go into section that contains headlines
        section = soup.find_all('section')
        articles = section[1].find_all('article')  # list of all article tags
        for i in range(15):  # get top 15 articles
            headline = articles[i].find('span', {'class': 'cd__headline-text'})
            if headline is not None:
                title = headline.getText()
                # this will provide url parameters - we need to prepend cnn.com to front
                href = articles[i].find('a')['href']
                url = f'https://cnn.com{href}'
                self.result.append({'title': title, 'url': url})
        return self.result

Cnn_Scraper().get_articles()

