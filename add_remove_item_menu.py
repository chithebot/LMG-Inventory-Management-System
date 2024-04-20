import add_item
import ims_tools
import main_menu
import menu
import remove_item
import state
import user_input


class AddRemoveItemMenu(menu.Menu, state.State):
    """ This class is the system object's add or remove item menu state.
    The user chooses whether or not they would like to add or remove an item.
    """

    """
    This function displays the add/remove item menu onto the console.

    Args:
        self (AddRemoveItemMenu) : the current AddRemoveItemMenu object
    """
    def displayMenu(self):

        # Displaying add/remove item menu items
        print("1. Add Item\n"
              "2. Remove Item\n"
              "3. Back\n")


    """
    This function updates the system object's state given the user's
    inputs to interact with the add or remove item menu.

    Args:
        self (AddRemoveItemMenu) : the current AddRemoveItemMenu object
        system (System)          : the System object of interest
    """
    def update(self, system):

        # Possible states
        states = {1: add_item.AddItem, 2: remove_item.RemoveItem, 3: main_menu.MainMenu}

        # Displaying add/remove item menu and getting user input
        ims_tools.newScreen()
        self.displayMenu()
        userInput = user_input.getIntRange("Enter your choice: ", 1, len(states) + 1)
        system.changeState(states[userInput]())