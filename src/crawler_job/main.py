import logging

from crawler import Crawler
from url_metrics import UrlMetrics
from database import  Database

MAXIMUM_DEGREE_DEPTH = 5


def lambda_handler(event, context):

    logging.info(event)
    logging.info(context)

    # TODO: get from dynamodbTable
    db = Database()
    print(db.get_items())
    
    _urls = ['https://scrapethissite.com/', 'http://www.example.com/']

    logging.info('Processing urls')

    Crawler(urls=_urls, maximum_degree_depth = MAXIMUM_DEGREE_DEPTH).run()

    # Load json lines to a dict-list
    logging.info('Processing url metrics')

    UrlMetrics().generate_metrics()


if __name__ == '__main__':

    lambda_handler({}, {})