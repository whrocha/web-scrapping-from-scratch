import logging

from crawler import Crawler
from url_metrics import UrlMetrics

MAXIMUM_DEGREE_DEPTH = 10

URLS = [
    'https://scrapethissite.com/',
    'http://www.example.com/',
]

def run_crawler():

    logging.info('Processing urls')

    Crawler(urls=URLS, maximum_degree_depth = MAXIMUM_DEGREE_DEPTH).run()

    # Load json lines to a dict-list
    logging.info('Processing url metrics')

    UrlMetrics().generate_metrics()


if __name__ == '__main__':

    run_crawler()