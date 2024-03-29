import abc


class Database(abc.ABC):
    """
    This is an abstract class for a database.

        Attributes:
            _filename (string) : the filename of the database (also contains the path)
    """

    """
    This function intializes a Database object.

    Args:
        self (Database)	    : the current Database object
        filename (string)	: the filename of the database
    """
    def __init__(self, filename=""):
        self._filename = filename


    """
    This function gets the current Database object's filename.

    Args:
        self (Database)	: the current Database object

    Returns:
        Returns the filename stored in the current Database object.
    """
    @property
    def filename(self):
        return self._filename


    """
    This function sets the given filename to the current Database object's
    filename.

    Args:
        self (Database)	: the current Database object
        filename (type)	: the new filename
    """    
    @filename.setter
    def filename(self, filename):
        self._filename = filename


    """
    This is an abstract function which reads the data, from the file at the
    given filename, into the Database object.

    Args:
        self (Database) : the current Database object
    """
    @abc.abstractmethod
    def readData(self):
        pass


    """
    This is an abstract function which saves the data, from the current Database
    object, into the file at the given filename.

    Args:
        self (Database) : the current Database object
    """
    @abc.abstractmethod
    def saveData(self):
        pass
