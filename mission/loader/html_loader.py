from .base import BaseParser
from urllib import request

from . import exception


class BaseHTMLLoader(BaseParser):
    HTML_MAIN_URL = None

    def __init__(self, parser, url):
        self._parser = parser
        self.check(url)
        self._url = url

    def check(self, url):
        if self.HTML_MAIN_URL not in url:
            raise exception.CheckURLError('Incorrect url')
    
    def parse(self):
        html_page = request.urlopen(self._url)
        self._parser.feed(str(html_page.read()))


class GoogleAppLoader(BaseHTMLLoader):
    HTML_MAIN_URL = 'https://play.google.com/'
