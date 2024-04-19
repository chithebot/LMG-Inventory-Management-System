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
        return iter(self.db)


    """
    This function returns the length of the list.

    Args:
        self (ListDatabase) : the current ListDatabase object

    Returns:
        Returns the length of the ListDatabase's list. 
    """
    def __len__(self):
        return len(self.db)
    

    """
    This function returns the value associated with the given
    key, or index, in the list.

    Args:
        self (ListDatabase) : the current ListDatabase object

    Returns:
        Returns the value, associated with the given key, or
        index, in the ListDatabase's list. 
    """
    def __getitem__(self, key):
        return self.db[key]
    

    """
    This function returns the index, associated with the given
    element, in the list.

    Args:
        self (ListDatabase) : the current ListDatabase object

    Raises:
        ValueError : Raised if the element does not exist in list.

    Returns:
        Returns the index, associated with the given element, or
        value, in the ListDatabase's list. 
    """
    def index(self, element):
        return self.db.index(element)


    """
    This function returns a boolean value indicating if the
    database is empty. Returns True if empty; otherwise, False
    is returned.

    Args:
        self (ListDatabase) : the current ListDatabase object

    Returns:
        Returns True if the database is empty; False, otherwise.
    """
    def empty(self):
        return not self.db
    

    """
    This function sets the given value to the key location
    in the list.

    Args:
        self (ListDatabase) : the current ListDatabase object
    """
    def __setitem__(self, key, value):
        self.db[key] = value


    """
    This function removes a given element from the list.

    Args:
        self (ListDatabase) : the current ListDatabase object
        element (T)         : the element to remove

    Raises:
        ValueError : Raised if element does not exist in list
    """
    def remove(self, element):
        self.db.remove(element)


    """
    This is removes an element, at the given index, from the list
    and returns the removed element.

    Args:
        self (ListDatabase) : the current ListDatabase object
        element (T)         : the element to remove

    Raises:
        IndexError : Raised if index is out of bounds
    
    Returns:
        Returns the element that was removed.
    """
    def pop(self, index):
        return self.db.pop(index)


    """
    This is an function which clears the data from the current ListDatabase
    object's list.

    Args:
        self (ListDatabase) : the current ListDatabase object
    """
    def clearData(self):
        self.db.clear()


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