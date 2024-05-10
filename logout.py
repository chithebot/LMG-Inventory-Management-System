import start_menu
import state


class Logout(state.State):
    """ This class is the system object's logout state which the user
    is logged out from the system. The system data is solved and current
    user data is wiped in this state.
    """

    """
    This function handles logging the user out of the given system. 

    Args:
        self (Logout)   : the current Logout object
        system (System) : the System object of interest
    """
    def update(self, system):
        
        # Saving category data only if a category change has been detected
        if system.categoryChange:
            system.catdb.sort()
            system.catdb.saveData()
        
        # Saving item data only if a item change has been detected
        if system.itemChange:
            system.itemdb.sortBySKU()
            system.itemdb.saveData()

        # Clearing all existing data
        system.clearCurrentUser()
        system.itemdb.clearData()
        system.catdb.clearData()

        # Resetting system status' for next user login
        system.resetStatus()

        # Moving back to start menu
        system.changeState(start_menu.StartMenu())