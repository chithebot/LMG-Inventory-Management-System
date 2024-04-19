import state
import tools


class Exit(state.State):
    """ This class is the system object's state where the system exit
    status is triggered.
    """

    """
    This function updates the system object's saves all system data then
    sets the system exit status to on.

    Args:
        self (Exit)     : the current Exit object
        system (System) : the System object of interest
    """
    def update(self, system):

        tools.clearScreen()
        system.exit = True