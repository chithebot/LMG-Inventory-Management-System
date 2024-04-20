import time

import ims_tools
import start_menu
import state
import tools


class Introduction(state.State):
    """ This class is the system object's state where the trademark screen
    is displayed.
    """

    """
    This function displays the software title and trademark onto the console
    then changes the system state to the start menu.

    Args:
        self (Introduction) : the current Introduction object
        system (System)     : the System object of interest
    """
    def update(self, system):

        # Clearing terminal screen
        tools.clearScreen()

        # Opening file containing title header
        ims_tools.displayTitle()
        time.sleep(3.5)
        tools.clearScreen()

        # Opening file containing group
        ims_tools.displayDevGroup()
        time.sleep(3.5)
        tools.clearScreen()

        # Changing the system state
        system.changeState(start_menu.StartMenu())