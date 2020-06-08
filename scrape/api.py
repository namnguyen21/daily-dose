import mysql.connector
from pymongo import MongoClient
from Fox_Scraper import Fox_Scraper
from Reddit_Scraper import Reddit_Scraper
from Cnn_Scraper import Cnn_Scraper
from NYT_Scraper import NYT_Scraper
from ESPN_Scraper import ESPN_Scraper
from Si_Scraper import Si_Scraper
from Bleacher_Scraper import Bleacher_Scraper
from youtube import Youtube
from Giphy import Giphy
from Usa_Scraper import Usa_Scraper
from NPR_Scraper import NPR_Scraper

client = MongoClient('localhost', 27017)

db = client.dailydose

# collections
news = db.news
sports = db.sports
media = db.media


def store_news():
    reddit = Reddit_Scraper().get_posts()
    fox = Fox_Scraper().get_articles()
    cnn = Cnn_Scraper().get_articles()
    nyt = NYT_Scraper().get_articles()
    usa = Usa_Scraper().get_articles()
    npr = NPR_Scraper().get_articles()
    # delete all existing posts
    news.update_many({} , {'$set': {'data': []}})
    for i in range(15):
        news.update_one({"name": 'fox'}, {'$push': {'data': fox[i]}})
        news.update_one({"name": 'reddit'}, {'$push': {'data': reddit[i]}})
        news.update_one({'name': 'cnn'}, {'$push': {'data': cnn[i]}})
    for article in nyt:
        news.update_one({'name': 'new york times'},
                        {'$push': {'data': article}})
    for article in usa: 
        news.update_one({'name': 'usa today'}, {'$push': {'data': article}}, True)
    for article in npr: 
        news.update_one({'name': 'npr'}, {'$push': {'data': article}},  True)
    


def store_sports():
    espn = ESPN_Scraper().get_articles()
    si = Si_Scraper().get_articles()
    bleacher = Bleacher_Scraper().get_articles()
    sports.update_one({'name': 'espn'}, {'$set': {'data': []}})
    sports.update_one({'name': 'sports illustrated'}, {'$set': {'data': []}})
    sports.update_one({'name': 'bleacher report'}, {'$set': {'data': []}})
    for article in espn:
        sports.update_one({'name': 'espn'}, {'$push': {'data': article}})
    for article in si:
        sports.update_one({'name': 'sports illustrated'},
                          {'$push': {'data': article}})
    for article in bleacher:
        sports.update_one({'name': 'bleacher report'},
                          {'$push': {'data': article}})


def store_media():
    youtube = Youtube().get_videos()
    giphy = Giphy().get_gifs()
    # clear existing results
    media.update_one({'name': 'youtube'}, {'$set': {'data': []}})
    media.update_one({'name': 'giphy'}, {'$set': {'data': []}})
    for video in youtube:
        media.update_one({'name': 'youtube'},
                         {'$push': {'data': video}})
    for gif in giphy:
        media.update_one({'name': 'giphy'},
                         {'$push': {'data': gif}})


def main():
    store_news()
    store_sports()
    store_media()
    print('saved to mongo')


main()
