import abc

import database


class DictDatabase(database.Database, abc.ABC):
    """ This abstract class is a database with a dictonary as its container.

        Attributes:
            _db (dict) : a dictionary which will be used to contain the data
    """
    __doc__ += ('\n' + database.Database.__doc__)


    """
    This function initializes a DictDatabase object.

    Args:
        self (DictDatabase) : the current DictDatabase object
        filename (string)   : the filename to the database
    """
    def __init__(self, filename=""):
        super().__init__(filename)
        self._db = {}


    """
    This function gets the database stored in the DictDatabase object.

    Args:
        self (DictDatabase) : the current DictDatabase object

    Returns:
        Returns the database (or dictionary) containing data.
    """   
    @property
    def db(self):
        return self._db


    """
    This function returns an iterator to the dictionary, or database, containing
    the data.

    Args:
        self (DictDatabase) : the current DictDatabase object

    Returns:
        Returns an iterator to the DictDatabase's dictionary. 
    """
    def __iter__(self):
        return self.db.__iter__()


    """
    This is an abstract function which reads the data, from the file at the
    given filename, into the DictDatabase object.

    Args:
        self (DictDatabase) : the current DictDatabase object
    """
    @abc.abstractmethod
    def readData(self):
        pass


    """
    This is an abstract function which saves the data, from the current DictDatabase
    object, into the file at the given filename.

    Args:
        self (DictDatabase) : the current DictDatabase object
    """
    @abc.abstractmethod
    def saveData(self):
        pass
