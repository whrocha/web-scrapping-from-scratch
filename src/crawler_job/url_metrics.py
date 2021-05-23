import logging
import json
import requests

from bs4 import BeautifulSoup


class UrlMetrics():

    def __init__(self):

        self.rows = []

    def generate_metrics(self):

        with open('/tmp/items.jl') as f:

            for line in f:

                self.rows.append(json.loads(line))

        i = 0

        rows = self.rows

        for row in rows:
            
            logging.info(f'Processing link {i} of {len(rows)-1}')
            
            # Make a GET request to fetch the raw HTML content
            response = requests.get(row['link'])
            
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
            
            i += 1

        # TODO: save url to dynamodb
        
        print(self.rows)