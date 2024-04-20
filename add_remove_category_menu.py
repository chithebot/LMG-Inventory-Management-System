import add_category
import ims_tools
import main_menu
import menu
import remove_category
import state
import user_input


class AddRemoveCategoryMenu(menu.Menu, state.State):
    """ This class is the system object's add or remove category menu state.
    The user chooses whether or not they would like to add or remove an category.
    """

    """
    This function displays the add/remove category menu onto the console.

    Args:
        self (AddRemoveCategoryMenu) : the current AddRemoveCategoryMenu object
    """
    def displayMenu(self):

        # Displaying add/remove item menu items
        print("1. Add Category\n"
              "2. Remove Category\n"
              "3. Back\n")


    """
    This function updates the system object's state given the user's
    inputs to interact with the add or remove category menu.

    Args:
        self (AddRemoveCategoryMenu) : the current AddRemoveCategoryMenu object
        system (System)              : the System object of interest
    """
    def update(self, system):

        # Possible states
        states = {1: add_category.AddCategory, 2: remove_category.RemoveCategory, 3: main_menu.MainMenu}

        # Displaying add/remove category menu and getting user input
        ims_tools.newScreen()
        self.displayMenu()
        userInput = user_input.getIntRange("Enter your choice: ", 1, len(states) + 1)
        system.changeState(states[userInput]())