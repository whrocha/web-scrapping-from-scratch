import requests

# Get endpoint from building stack
API_ENDPOINT = 'https://9fbw9zo3qh.execute-api.us-east-1.amazonaws.com/Prod/crawler/'


def run():

    url = 'https://www.google.com/'

    param = {
        'url': url
    }

    response = requests.get(API_ENDPOINT, params=param)

    print(response.text)

if __name__ == '__main__':

    run()