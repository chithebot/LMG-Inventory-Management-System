import entity


class User(entity.Entity):
    """ This class represents a user.

        Attributes:
            _username (string)  : the user's username
            _password (string)  : the user's password
    """
    __doc__ += ('\n' + entity.Entity.__doc__)


    """
    This function initializes an User object.

    Args:
        self (User)		    : the current User object
        name (string)	    : the name of the User object
        username (string)	: the username of the User object
        password (string)	: the password of the User object
    """ 
    def __init__(self, name="", username=""):
        super().__init__(name)
        self._username = username


    """
    This function gets the User object's username.

    Args:
        self (User) : the current User object
    
    Returns:
        Returns the User object's username.
    """ 
    @property
    def username(self):
        return self._username


    """
    This function sets the User object's username.

    Args:
        self (User)		    : the current User object
        username (string)	: the new username to set
    """ 
    @username.setter
    def username(self, username):
        self._username = username


    """
    This function sets all of the current User object's
    attributes to empty strings, or clears them.

    Args:
        self (User)		    : the current User object
        username (string)	: the new username to set
    """ 
    def clear(self):
        self.username = str()
        self.name = str()


    """
    This function returns the string representation of the current
    User object.

    Args:
        self (User)	: the current User object

    Returns:
        Returns a string which represents the current User object.
    """
    def __str__(self):
        return super().__str__() + "\t" + self.username