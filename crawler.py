import logging
import requests
import json

from urllib.parse import urljoin
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)


class Crawler:

    def __init__(self, urls=[]):

        self.visited_urls = []
        self.urls = []
        self.urls_to_visit = urls
        self.MAXIMUM_DEGREE_DEPTH = 20

    def get_linked_urls(self, url, html):
        """Get linked URLs from URL"""

        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all('a'):

            path = link.get('href')

            path = urljoin(url, path)

            yield path

    def add_url_to_visit(self, url):
        """Add url to visited urls"""

        if url not in self.visited_urls and url not in self.urls_to_visit:

            self.urls_to_visit.append(url)

    def crawl(self, url):
        """Crawl url"""

        html = requests.get(url).text

        dict_url = {}
        dict_url['url'] = url
        dict_url['content'] = html
        self.urls.append(dict_url)

        for url in self.get_linked_urls(url, html):

            self.add_url_to_visit(url)

    def run(self):
        """Run crawler""" 

        self.depth = 0

        while self.urls_to_visit and self.depth <= self.MAXIMUM_DEGREE_DEPTH:

            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')

            try:

                self.crawl(url)

            except Exception:

                logging.exception(f'Failed to crawl: {url}')

            finally:

                self.visited_urls.append(url)
                self.depth += 1

        self.process_items()

    def process_items(self):
        """Process extracted items to find appearences"""

        logging.info('Processing extracted links')

        rows = []

        for item in self.urls:

            soup = BeautifulSoup(item['content'], 'lxml')

            line_item = {}
            
            line_item['link'] = item['url']

            # links
            line_item['links'] = [t.get('href') for t in soup.find_all('a') if 'http' in t.get('href',[])]

            rows.append(line_item)

        with open('items.jl', 'w') as f:
            
            for row in rows:

                l = [tt for tt in [t for t in rows if row['link'] not in t['link']] if row['link'] in tt['links']]

                row['appearences'] = len(l)

                row_copy = row.copy()
                row_copy.pop('links', None)

                f.write(json.dumps(row_copy) + "\n")


if __name__ == '__main__':

    Crawler(urls=['https://scrapethissite.com/']).run()