from abc import ABC, abstractmethod


class BaseParser(ABC):
    @abstractmethod
    def parse_appartments_list(self, url=None):
        pass


    @abstractmethod
    def get_request(self, url=None):
        pass