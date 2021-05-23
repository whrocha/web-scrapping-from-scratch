import requests
import logging

from pynamodb.connection import TableConnection
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute
)
from bs4 import BeautifulSoup


# Create table model to be save on Dynamo
class TableUrlCrawler(Model):
        class Meta:
            table_name = ''

        link = UnicodeAttribute(hash_key=True)
        appearences = NumberAttribute(default=0)
        qty_character_url = NumberAttribute(default=0)
        qty_character_page_title = NumberAttribute(default=0)
        qty_page_http_links = NumberAttribute(default=0)
        qty_page_internal_links = NumberAttribute(default=0)
        qty_total_a = NumberAttribute(default=0)
        qty_total_table = NumberAttribute(default=0)
        qty_total_table_tr = NumberAttribute(default=0)
        qty_total_table_td = NumberAttribute(default=0)
        qty_bytes_response = NumberAttribute(default=0)
        qty_h1_page = NumberAttribute(default=0)

        @staticmethod
        def setup_model(model, table_name):
            model.Meta.table_name = table_name

def __save(rows, table_name):

    logging.info("Saving {rows}")

    TableUrlCrawler.setup_model(TableUrlCrawler, table_name)

    for row in rows:

        link = row['link']

        logging.info(f'Saving url {link}')

        table_url_crawler = TableUrlCrawler()
        table_url_crawler.link = link
        table_url_crawler.qty_character_url = int(row['qty_character_url'])
        table_url_crawler.qty_character_page_title = row['qty_character_page_title']
        table_url_crawler.qty_page_http_links = row['qty_page_http_links']
        table_url_crawler.qty_page_internal_links = row['qty_page_internal_links']
        table_url_crawler.qty_total_a = row['qty_total_a']
        table_url_crawler.qty_total_table = row['qty_total_table']
        table_url_crawler.qty_total_table_tr = row['qty_total_table_tr']
        table_url_crawler.qty_total_table_td = row['qty_total_table_td']
        table_url_crawler.qty_bytes_response = row['qty_bytes_response']
        table_url_crawler.qty_h1_page = row['qty_h1_page']

        table_url_crawler.save()

def get_url(url, table_table):

    logging.info("Get a table connection")
    table = TableConnection(table_table)

    logging.info(f"Get {url} item")
    payload = table.get_item(url)

    # if url doen't exists build metrics based on html content
    if payload.get('Item', {}) == {}:

        row = {}
        
        # set url
        row['link'] = url

        # Make a GET request to fetch the raw HTML content
        response = requests.get(url)

        html_content = response.text

        # Parse the html content
        soup = BeautifulSoup(html_content, "lxml")
        
        # Vector #1 - URL character Length
        row['qty_character_url'] = len(row['link'])

        # Vector #2: Page Title Character Length
        row['qty_character_page_title'] = 0 if soup.html.head == None else len(soup.html.head.title.text)
        
        # Vector #3: Page href http(s) qty
        row['qty_page_http_links'] = len([t for t in soup.find_all('a') if 'http' in t.get('href',[]) ])
        
        # Vector #4: Page internal links qty
        row['qty_page_internal_links'] = len([t for t in soup.find_all('a')  if 'http' not in t.get('href',[])])
        
        # Vector #5: Qty a html tag
        row['qty_total_a'] = len(soup.find_all('a'))
        
        # Vector #6: Qty <table>
        row['qty_total_table'] = len(soup.find_all("table"))
        
        # Vector #7: Qty tr
        row['qty_total_table_tr'] = len(soup.find_all("tr"))
        
        # Vector #8: Qty table td
        row['qty_total_table_td'] = len(soup.find_all("td"))
        
        # Vector #9: Response Size
        row['qty_bytes_response'] = len(response.content)
        
        # Vector #10: Qty Page H1
        row['qty_h1_page'] = len(soup.find_all("h1"))

        __save([row],table_table)

        while payload.get('Item', {}) == {}:
            
            # get saved url
            payload = table.get_item(url)


    return payload['Item']
