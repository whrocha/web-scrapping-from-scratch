import requests

# Get endpoint from building stack
API_ENDPOINT = 'https://9fbw9zo3qh.execute-api.us-east-1.amazonaws.com/Prod/crawler/'
URL = 'https://www.google.com/'

def run():

    param = {
        'url': URL
    }

    response = requests.get(API_ENDPOINT, params=param)

    print(response.text)

if __name__ == '__main__':

    run()