import abc

import database


class ListDatabase(database.Database, abc.ABC):
    """ This abstract class is a database with a list/array as its container.

        Attributes:
            _db (list) : a list which will be used to contain the data
    """
    __doc__ += ('\n' + database.Database.__doc__)


    """
    This function initializes a ListDatabase object.

    Args:
        self (ListDatabase) : the current ListDatabase object
        filename (string)   : the filename to the database
    """
    def __init__(self, filename=""):
        super().__init__(filename)
        self._db = []


    """
    This function gets the database stored in the ListDatabase object.

    Args:
        self (ListDatabase) : the current ListDatabase object

    Returns:
        Returns the database (or list) containing data.
    """
    @property
    def db(self):
        return self._db


    """
    This function returns an iterator to the list, or database, containing
    the data.

    Args:
        self (ListDatabase) : the current ListDatabase object

    Returns:
        Returns an iterator to the ListDatabase's list. 
    """
    def __iter__(self):
        return self.db.__iter__()


    """
    This is an abstract function which reads the data, from the file at the
    given filename, into the ListDatabase object.

    Args:
        self (ListDatabase) : the current ListDatabase object
    """
    @abc.abstractmethod
    def readData(self):
        pass


    """
    This is an abstract function which saves the data, from the current ListDatabase
    object, into the file at the given filename.

    Args:
        self (ListDatabase) : the current ListDatabase object
    """
    @abc.abstractmethod
    def saveData(self):
        pass
