class Entity:
    """ This is a basic entity class.

        Attributes:
            _name (string) : the name of the Entity object
    """
    
    """
    This function intializes an Entity object.

    Args:
        self (Entity)	: the current Entity object
        name (string)	: the name of the Entity object
    """
    def __init__(self, name=""):
        self._name = name


    """
    This function gets the current Entity object's name.

    Args:
        self (Entity)	: the current Entity object

    Returns:
        Returns a string which is the name of the Entity object.
    """
    @property
    def name(self):
        return self._name


    """
    This function sets the current Entity object's name to the
    passed in name.

    Args:
        self (Entity)	: the current Entity object
        name (string)	: the new name of the Entity object
    """
    @name.setter
    def name(self, name):
        self._name = name


    """
    This function returns the string representation of the current
    Entity object.

    Args:
        self (Entity)	: the current Entity object

    Returns:
        Returns a string which represents the current Entity object.
    """
    def __str__(self):
        return self.name