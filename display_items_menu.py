import display_items_all as dia
import display_items_category as dic
import ims_tools
import main_menu
import menu
import state
import user_input


class DisplayItemsMenu(menu.Menu, state.State):
    """ This class is the system object's display items menu state. The user
    chooses whether or not they would like to add or remove an category.
    """

    """
    This function displays the display items menu onto the console.

    Args:
        self (DisplayItemMenu) : the current DisplayItemMenu object
    """
    def displayMenu(self):

        # Displaying the display item menu items
        print("1. Display All Items\n"
              "2. Display Items by Specific Category\n"
              "3. Back\n")


    """
    This function updates the system object's state given the user's
    inputs to interact with the display items menu.

    Args:
        self (DisplayItemMenu) : the current DisplayItemMenu object
        system (System)        : the System object of interest
    """
    def update(self, system):

        # Possible states
        states = {1: dia.DisplayItemsAll, 2: dic.DisplayItemsCategory, 3: main_menu.MainMenu}

        # Displaying display items menu and getting user input
        ims_tools.newScreen()
        self.displayMenu()
        userInput = user_input.getIntRange("Enter your choice: ", 1, len(states) + 1)
        system.changeState(states[userInput]())