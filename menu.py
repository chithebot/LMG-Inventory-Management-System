import abc


class Menu(abc.ABC):
    """ This is an interface for a displayed menu.
    """
    
    """
    This is an abstract function which is to be implemented to display the
    current Menu object's menu options.

    Args:
        self (Menu) : the current Menu object
    """
    @abc.abstractmethod
    def displayMenu(self):
        pass