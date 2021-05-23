import logging
import database
import os


def lambda_handler(event, context):

    logging.basicConfig(
        format='%(asctime)s %(levelname)s:%(message)s',
        level=logging.INFO
    )

    logging.info(event)
    logging.info(context)
       
    url = event['url']

    table_name = os.getenv('TABLE_NAME', 'table-url-crawler')

    url_detail = database.get_url(url, table_name)

    logging.info(url_detail)

    return url_detail


if __name__ == '__main__':

    event = {
        # 'url': 'https://pynamodb.readthedocs.io/en/latest/tutorial.html'
        'url': 'https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tablename'
    }

    lambda_handler(event, {})