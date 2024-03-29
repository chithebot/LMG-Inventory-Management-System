import abc

import database


class ListDatabase(database.Database, abc.ABC):
    
    def __init__(self, filename=""):
        super().__init__(filename)
        self._db = []
    
    @property
    def db(self):
        return self._db

    def __iter__(self):
        return self.db.__iter__()

    @abc.abstractmethod
    def readData(self):
        pass

    @abc.abstractmethod
    def saveData(self):
        pass
