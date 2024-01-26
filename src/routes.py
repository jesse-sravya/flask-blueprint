import requests

from urllib.parse import urljoin
from flask import Blueprint, jsonify, request
from src.helper import get_top_words, get_stop_words

# constants
URL = 'https://en.wikipedia.org/api/rest_v1/page/summary/'
STOP_WORDS_FILE = 'stopwords.txt'
DEFAULT_LIMIT = 10
CONTENT_KEY = 'extract'

STOP_WORDS = get_stop_words(STOP_WORDS_FILE)
routes = Blueprint('routes', __name__)


@routes.route("/health")
def health_check():
    return "OK!"


@routes.route("/fetch/<string:article_name>")
def fetch(article_name):
    if not article_name and len(article_name) == 0:
        return jsonify({ 'success': False, 'message': f"{article_name} is not a proper input" }), 400

    limit = request.args.get('limit')
    if limit and limit.isdigit():
        limit = int(limit)
    else:
        limit = DEFAULT_LIMIT
    response = requests.get(url = urljoin(URL, article_name))

    if response.status_code != 200:
        return jsonify({ 'success': False, 'message': "wikipedia hasn't returned a valid response" })
    
    text = response.json()
    return jsonify({ 'success': True, 'data': get_top_words(text.get(CONTENT_KEY, ''), limit, STOP_WORDS) })

