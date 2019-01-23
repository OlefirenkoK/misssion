from html.parser import HTMLParser


class BaseHTMLParser(HTMLParser):
    def __init__(self, category, *args, **kwargs):
        super(BaseHTMLParser, self).__init__(*args, **kwargs)
        self._category = category

    def handle_starttag(self, tag, attrs):
        if tag == 'a' and ('class', 'title-link id-track-click') in attrs:
            self._category.find()

        if tag == 'a' and ('class', 'card-click-target') in attrs:
            try:
                self._category.add_game(attrs)
            except ValueError as exc:
                print(exc)
                print('Unexpected tag found')

    def handle_data(self, data):
        if self._category.status:
            self._category.add(data)


class GoogleAppHTMLParser(BaseHTMLParser):
    pass
