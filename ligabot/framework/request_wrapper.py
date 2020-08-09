import requests

def get_webpage_content(url):
    response = requests.get(url)
    return response.content
