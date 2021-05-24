import database
import os
import json

def lambda_handler(event, context):

    print(event)
    print(context)
       
    url = event.get('queryStringParameters',{}).get('url')

    print(url)

    table_name = os.getenv('TABLE_NAME', 'table-url-crawler')

    url_detail = database.get_url(url, table_name)

    print(url_detail)

    payload_return = {
        "statusCode": 200,
        "body": json.dumps(url_detail),
    }

    return payload_return


if __name__ == '__main__':

    # event-test
    event = {'resource': '/crawler', 'path': '/crawler/', 'httpMethod': 'GET', 'headers': {'Accept': '*/*', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'BR', 'Host': '9fbw9zo3qh.execute-api.us-east-1.amazonaws.com', 'User-Agent': 'curl/7.68.0', 'Via': '2.0 321b77cb7808dc2de3eb3940d5be0349.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'n8-nuogj1rkQ_pygwBRqxJzhNLbbD6ZRQ4AEgd15FYDxz-r5HOLnWQ==', 'X-Amzn-Trace-Id': 'Root=1-60ab0774-054780786116f421753603e1', 'X-Forwarded-For': '191.177.172.182, 130.176.160.184', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Accept': ['*/*'], 'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-Country': ['BR'], 'Host': ['9fbw9zo3qh.execute-api.us-east-1.amazonaws.com'], 'User-Agent': ['curl/7.68.0'], 'Via': ['2.0 321b77cb7808dc2de3eb3940d5be0349.cloudfront.net (CloudFront)'], 'X-Amz-Cf-Id': ['n8-nuogj1rkQ_pygwBRqxJzhNLbbD6ZRQ4AEgd15FYDxz-r5HOLnWQ=='], 'X-Amzn-Trace-Id': ['Root=1-60ab0774-054780786116f421753603e1'], 'X-Forwarded-For': ['191.177.172.182, 130.176.160.184'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': {'url': 'http://www.example.com/'}, 'multiValueQueryStringParameters': {'url': ['http://www.example.com/']}, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': '4nzthv', 'resourcePath': '/crawler', 'httpMethod': 'GET', 'extendedRequestId': 'fz4aPHFLIAMFy9Q=', 'requestTime': '24/May/2021:01:55:00 +0000', 'path': '/Prod/crawler/', 'accountId': '163212085100', 'protocol': 'HTTP/1.1', 'stage': 'Prod', 'domainPrefix': '9fbw9zo3qh', 'requestTimeEpoch': 1621821300678, 'requestId': '45cb1232-1c23-4e1c-a955-c7cbbbb9f498', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '191.177.172.182', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'curl/7.68.0', 'user': None}, 'domainName': '9fbw9zo3qh.execute-api.us-east-1.amazonaws.com', 'apiId': '9fbw9zo3qh'}, 'body': None, 'isBase64Encoded': False}
    event = {
        'queryStringParameters': {
            'url': 'http://www.example.com/'
        }
    }

    lambda_handler(event, {})