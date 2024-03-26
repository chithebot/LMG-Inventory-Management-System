import abc


class State(abc.ABC):

    @abc.abstractmethod
    def update():
        pass
