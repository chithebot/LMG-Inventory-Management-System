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
        return iter(self.db)


    """
    This function returns the length of the dictionary.

    Args:
        self (DictDatabase) : the current DictDatabase object

    Returns:
        Returns the length of the DictDatabase's dictionary. 
    """
    def __len__(self):
        return len(self.db)


    """
    This function returns the value associated with the given
    key in the dictionary.

    Args:
        self (DictDatabase) : the current DictDatabase object
    
    Raises:
        KeyError : Raised if key does not exist in dictionary.

    Returns:
        Returns the value, associated with the given key, in
        the DictDatabase's dictionary. 
    """
    def __getitem__(self, key):
        return self.db[key]


    """
    This function returns the value associated with the given
    key in the dictionary. If no key is found, then None is
    returned by default. A default value can be defined.

    Args:
        self (DictDatabase) : the current DictDatabase object

    Returns:
        Returns the value, associated with the given key, in
        the DictDatabase's dictionary if it exists. Otherwise,
        a default value is returned. 
    """
    def get(self, key, default=None):
        return self.db.get(key, default)


    """
    This function returns a boolean value indicating if the
    database is empty. Returns True if empty; otherwise, False
    is returned.

    Args:
        self (DictDatabase) : the current DictDatabase object

    Returns:
        Returns True if the database is empty; False, otherwise.
    """
    def empty(self):
        return not self.db


    """
    This function sets the given value to the key location
    in the dictionary.

    Args:
        self (DictDatabase) : the current DictDatabase object
    """
    def __setitem__(self, key, value):
        self.db[key] = value


    """
    This function returns the value, associated with the given
    key, that was removed in the dictionary. If no key is found,
    then None is returned by default. A default value can be
    defined.

    Args:
        self (DictDatabase) : the current DictDatabase object

    Returns:
        Returns the value, associated with the given key, in
        the DictDatabase's dictionary if it was removed. Otherwise,
        a default value is returned. 
    """
    def pop(self, key, default=None):
        return self.db.pop(key, default)
        

    """
    This is an function which ckears the data from the current DictDatabase
    object's dictionary.

    Args:
        self (DictDatabase) : the current DictDatabase object
    """
    def clearData(self):
        self.db.clear()

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