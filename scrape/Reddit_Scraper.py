from bs4 import BeautifulSoup
import praw
from dotenv import load_dotenv
from pathlib import Path
import requests
from pprint import pprint
from time import sleep
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

REDDIT_14 = os.getenv('REDDIT_14')
REDDIT_27 = os.getenv('REDDIT_27')
REDDIT_USER = os.getenv('USERNAME')
REDDIT_PSWD = os.getenv('PASSWORD')


class Reddit_Scraper():
    def __init__(self):
        self.url = 'https://reddit.com/r/news'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.result = []  # end product will be list of dicts
        self.reddit = praw.Reddit(client_id=REDDIT_14,
                                  client_secret=REDDIT_27,
                                  user_agent='nam',
                                  username=REDDIT_USER,
                                  password=REDDIT_PSWD)
        # get top 15 posts from the news subreddit
        self.subreddit = self.reddit.subreddit('news').hot(limit=15)

    def get_posts(self):
        for submission in self.subreddit:
            self.result.append(
                {'title': submission.title, 'url': submission.url})
        return self.result

