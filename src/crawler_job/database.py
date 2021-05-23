import logging

from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute
)

# Create table model to be save on Dynamo
class TableUrlCrawler(Model):
        class Meta:
            table_name = 'table-url-crawler'

        link = UnicodeAttribute(hash_key=True)
        appearences = UnicodeAttribute(range_key=True)
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


def save(rows):

    for row in rows:

        link = row['link']

        logging.info(f'Saving url {link}')

        table_url_crawler = TableUrlCrawler()
        table_url_crawler.link = link
        table_url_crawler.appearences  = str(row['appearences'])
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
