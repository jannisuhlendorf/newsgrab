import json
from urllib.parse import urlencode
import requests

from resources import config

api_key = config['newsapi_key']
url_everything = config['newsapi_url']


def get_articles(sources=None, from_=None, to=None, page_size=100):
    params = {
        'page_size': page_size,
        'apiKey': api_key
    }
    if sources is not None:
        params['sources'] = sources
    if from_ is not None:
        params['from'] = from_
    if to is not None:
        params['to'] = to
    q = urlencode(params)
    res = requests.get(url_everything, params=q)
    if res.status_code != 200:
        raise Exception(res.content)
    return json.loads(res.content.decode('utf-8'))
