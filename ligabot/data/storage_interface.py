from abc import ABC
from abc import abstractmethod

class StorageInterface(ABC):

    @abstractmethod
    def load_matches(self):
        pass
