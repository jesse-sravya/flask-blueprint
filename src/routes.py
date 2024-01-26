import requests

from urllib.parse import urljoin
from flask import Blueprint, jsonify, request
from src.helper import get_top_words, get_stop_words, get_article

STOP_WORDS_FILE = 'stopwords.txt'
DEFAULT_LIMIT = 10

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

    status, content = get_article(article_name)
    if not status:
        return jsonify({ 'success': False, 'message': "wikipedia hasn't returned a valid response" })

    return jsonify({ 'success': True, 'data': get_top_words(content, limit, STOP_WORDS) })

