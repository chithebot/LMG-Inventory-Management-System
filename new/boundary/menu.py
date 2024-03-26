import abc


class Menu(abc.ABC):
    
    @abc.abstractmethod
    def display():
        pass
