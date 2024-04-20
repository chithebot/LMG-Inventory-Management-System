import abc


class State(abc.ABC):
    """ This is an interface for the states of the System object.
    """

    """
    This is an abstract function which is to be implemented to update the
    System object according to the current State object.

    Args:
        self (Menu)     : the current Menu object
        system (System) : the System object of interest
    """
    @abc.abstractmethod
    def update(self, system):
        pass