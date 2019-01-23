from .loader import Category, GoogleAppLoader
from .printer import Print
from .parser import GoogleAppHTMLParser


class get_games_app_category(object):
    def __init__(self, url):
        self._url = url

    def __call__(self):
        category = Category()
        parser = GoogleAppHTMLParser(category)
        loader = GoogleAppLoader(parser, self._url)
        loader.parse()
        return category.categories


class get_games_app_names(object):
    def __init__(self, url):
        self._url = url

    def __call__(self):
        category = Category()
        parser = GoogleAppHTMLParser(category)
        loader = GoogleAppLoader(parser, self._url)
        loader.parse()
        return category.games


def html_parser():
    url = 'https://play.google.com/store/apps/category/GAME'
    category = Category()
    parser = GoogleAppHTMLParser(category)
    loader = GoogleAppLoader(parser, url)
    loader.parse()
    printer = Print(category)
    return printer.log()
