from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractCategory(object, metaclass=ABCMeta):
    @abstractmethod
    def add(self, category):
        raise NotImplementedError

    @abstractmethod
    def add_game(self, game):
        raise NotImplementedError

    @abstractmethod
    def find(self):
        raise NotImplementedError

    @abstractmethod
    def released(self):
        raise NotImplementedError

    @abstractproperty
    def status(self):
        raise NotImplementedError

    @abstractproperty
    def categories(self):
        raise NotImplementedError

    @abstractproperty
    def games(self):
        raise NotImplementedError


class Category(AbstractCategory):
    def __init__(self):
        self._found = False
        self._category_map = dict()
        self._processed_category = None

    def find(self):
        self._found = True

    @property
    def status(self):
        return self._found

    def released(self):
        self._found = False

    def add(self, category):
        print(category, 'category')
        self._category_map.setdefault(category, [])
        self._processed_category = category
        self.released()

    def add_game(self, game):
        game = self._get_game_name(game)
        if game is None:
            return
        game = game.strip()
        if self._processed_category is None:
            raise ValueError('Category not fond')
        self._category_map[self._processed_category].append(game)

    @staticmethod
    def _get_game_name(attrs):
        for attr in attrs:
            if attr and attr[0] == 'aria-label':
                return attr[1]


    @property
    def categories(self):
        return list(self._category_map.keys())

    @property
    def games(self):
        games = list()
        for category, _games in self._category_map.items():
            games.extend(_games)
        return games

    def iter(self):
        for category, games in self._category_map.items():
            for game in games:
                yield '{}/{}'.format(category, game)
