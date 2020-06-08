import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

DEVELOPER_KEY = os.getenv('GOOGLE_API')

# AIzaSyClzL0C0wb-4Z6Ewq-iWYJMeiNhDwVCRBQ

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]



class Youtube():
    def __init__(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        self.youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY)

    def get_videos(self):
        request = self.youtube.videos().list(
            part="snippet,contentDetails,statistics",
            chart="mostPopular",
            maxResults=20,
            regionCode="US")
        response = request.execute()
        result = []
        for video in response['items']:
            video_id = video['id']
            title = video['snippet']['title']
            thumbnail = video['snippet']['thumbnails']['medium']['url']
            result.append(
                {'title': title, 'url': f'https://youtube.com/watch?v={video_id}', 'thumbnail': thumbnail})
        return result