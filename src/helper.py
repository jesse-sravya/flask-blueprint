import re
import requests

from urllib.parse import urljoin

URL = 'https://en.wikipedia.org/api/rest_v1/page/summary/'
CONTENT_KEY = 'extract'


def get_top_words(content, limit=10, stop_words=[]):
    content_array = re.split('\W+', content)
    content_array = list(filter(lambda x: x not in stop_words, [x.lower() for x in content_array]))

    freq_map = {}
    for word in content_array:
        if word in freq_map:
            freq_map[word] = freq_map[word] + 1
        else:
            freq_map[word] = 1

    freq_map = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    return list(map(lambda item: item[0], freq_map[:limit]))

def get_stop_words(file):
    with open(file) as f:
        return f.read().split('\n')

def get_article(article_name):
    response = requests.get(url = urljoin(URL, article_name))
    if response.status_code != 200:
        return False, None
    return True, response.json().get(CONTENT_KEY, '')
