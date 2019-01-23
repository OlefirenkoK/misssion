from abc import ABCMeta, abstractmethod


class AbstractLoader(object, metaclass=ABCMeta):
    @abstractmethod
    def parse(self, *args, **kwargs):  # real signature unknown
        """"""

    @abstractmethod
    def check(self, *args, **kwargs):  # real signature unknown
        """"""


class BaseParser(AbstractLoader):
    def parse(self, *args, **kwargs):
        raise NotImplementedError

    def check(self, *args, **kwargs):
        raise NotImplementedError
