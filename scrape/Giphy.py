import requests
import json
from pprint import pprint
# 2VvH0YaeuEwWyJSvoOc84zSnMGqDJWJj
response = requests.get('https://api.giphy.com/v1/gifs/trending?api_key=2VvH0YaeuEwWyJSvoOc84zSnMGqDJWJj&limit=1')

class Giphy(): 
    def __init__(self):
        self.response = requests.get('https://api.giphy.com/v1/gifs/trending?api_key=2VvH0YaeuEwWyJSvoOc84zSnMGqDJWJj&limit=15').text
    
    def get_gifs(self):
        # we must parse the response to json format
        json_data = json.loads(self.response)
        result = [] # return list of objects of gifs 
        for gif in json_data['data']: 
            gif_id = gif['id']
            title = gif['title']
            embed_url = gif['embed_url']
            url = gif['url']
            result.append({'id': gif_id, 'title': title, 'embed_url':embed_url, 'url': url})
        return result
