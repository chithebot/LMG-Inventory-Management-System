import abc


class Database(abc.ABC):

    def __init__(self, filename=""):
        self._filename = filename
    
    @property
    def filename(self):
        return self._filename
    
    @filename.setter
    def filename(self, filename):
        self._filename = filename

    @abc.abstractmethod
    def readData(self):
        pass

    @abc.abstractmethod
    def saveData(self):
        pass
