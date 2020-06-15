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
from NYT_Sports import NYT_Sports
from AP_Scraper import AP_Scraper
from Buzzfeed_Scraper import Buzzfeed_Scraper
from ET_Scraper import ET_Scraper
from Nbc_Scraper import Nbc_Scraper
from WSJ_Scraper import WSJ_Scraper
from Time_Scraper import Time_Scraper
from Reuters_Scraper import Reuters_Scraper
from Cbs_Scraper import Cbs_Scraper

client = MongoClient('localhost', 27017)

db = client.dailydose

# collections
news = db.news
sports = db.sports
media = db.media


def store_news():
    # init all scrapers
    reddit = Reddit_Scraper().get_posts()
    fox = Fox_Scraper('https://foxnews.com').get_articles()
    cnn = Cnn_Scraper().get_articles()
    nyt = NYT_Scraper('https://www.nytimes.com/').get_articles()
    usa = Usa_Scraper('https://www.usatoday.com/news').get_articles()
    npr = NPR_Scraper('https://npr.org').get_articles()
    ap = AP_Scraper('https://apnews.com/').get_articles()
    buzz = Buzzfeed_Scraper('https://www.buzzfeed.com/').get_articles()
    et = ET_Scraper('https://www.etonline.com/news').get_articles()
    nbc = Nbc_Scraper('https://www.nbcnews.com/').get_articles()
    wsj = WSJ_Scraper('https://www.wsj.com/').get_articles()
    time = Time_Scraper('https://time.com/').get_articles()
    reuters = Reuters_Scraper('https://www.reuters.com/').get_articles()
    cbs = Cbs_Scraper('https://www.cbsnews.com/').get_articles()
    # rewrite existing posts with new ones
    news.update_one({'name': 'reddit'}, {'$set': {'data': reddit}}, True)
    news.update_one({'name': 'fox'}, {'$set': {'data': fox}}, True)
    news.update_one({'name': 'cnn'}, {'$set': {'data': cnn}}, True)
    news.update_one({'name': 'new york times'}, {'$set': {'data': nyt}}, True)
    news.update_one({'name': 'usa today'}, {'$set': {'data': usa}}, True)
    news.update_one({'name': 'fox'}, {'$set': {'data': fox}}, True)
    news.update_one({'name': 'npr'}, {'$set': {'data': npr}}, True)
    news.update_one({'name': 'associated press'}, {'$set': {'data': ap}}, True)
    news.update_one({'name': 'buzzfeed'}, {'$set': {'data': buzz}}, True)
    news.update_one({'name': 'ET'}, {'$set': {'data': et}}, True)
    news.update_one({'name': 'nbc'}, {'$set': {'data': nbc}}, True)
    news.update_one({'name': 'wall street journal'},
                    {'$set': {'data': wsj}}, True)
    news.update_one({'name': 'time'}, {'$set': {'data': time}})
    news.update_one({'name': 'reuters'}, {'$set': {'data': reuters}}, True)
    news.update_one({'name': 'cbs'}, {'$set': {'data': cbs}}, True)


def store_sports():
    #init scrapers
    espn = ESPN_Scraper('https://www.espn.com/').get_articles()
    si = Si_Scraper('https://www.si.com/').get_articles()
    bleacher = Bleacher_Scraper(
        'https://bleacherreport.com/featured').get_articles()
    nyt = NYT_Sports('https://www.nytimes.com/section/sports').get_articles()
    # rewrite existing posts with new ones
    sports.update_one({'name': 'espn'}, {'$set': {'data': espn}}, True)
    sports.update_one({'name': 'sports illustrated'},
                      {'$set': {'data': si}}, True)
    sports.update_one({'name': 'bleacher report'}, {
                      '$set': {'data': bleacher}}, True)
    sports.update_one({'name': 'new york times'}, {
                      '$set': {'data': nyt}}, True)


def store_media():
    youtube = Youtube().get_videos()
    giphy = Giphy().get_gifs()
    # clear existing results
    media.update_one({'name': 'youtube'}, {'$set': {'data': youtube}})
    media.update_one({'name': 'giphy'}, {'$set': {'data': giphy}})


def main():
    store_news()
    store_sports()
    store_media()
    print('saved to mongo')


main()
