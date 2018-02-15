import argparse
import logging

from newsgrab.database import DB
from newsgrab.newsapi import get_articles
from resources import config


max_requests = config['newsapi_max_no_requests']


class NewsGrabber:

    def __init__(self):
        self.db = DB()
        self.logger = logging.getLogger(__name__)

    def grab_newsapi_articles(self, sources=None):
        oldest = None
        for _ in range(max_requests):
            articles = get_articles(sources=sources, to=oldest)
            known_articles = 0
            for article in articles['articles']:
                if not self.db.id_exists(article['url']):
                    self.db.index_document(article, article['url'])
                    oldest = article['publishedAt']
                    self.logger.debug(article)
                else:
                    known_articles += 1
            if len(articles['articles']) == known_articles:
                break


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--newsapi-sources',
        help='sources to grab from newsapi.org',
        default=config['newsapi_sources']
    )
    parser.add_argument(
        '--logfile',
        help='logfile path',
        default='newsgrab.log'
    )
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR' or 'CRITICAL'],
        help='default: WARNING',
        default='WARNING'
    )
    args = parser.parse_args()
    logging.basicConfig(filename='newsgrab.log', level=getattr(logging, args.log_level))

    ng = NewsGrabber()
    ng.grab_newsapi_articles(sources=args.newsapi_sources)
