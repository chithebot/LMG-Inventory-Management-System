import add_remove_category_menu as arcm
import add_remove_item_menu as arim
import display_items_menu as dim
import edit_item_menu as eim
import ims_tools
import logout
import menu
import search_items as si
import state
import user_input


class MainMenu(menu.Menu, state.State):
    """ This class is the system object's state where the main menu is 
    displayed and the user interacts with to move to other system states.
    """

    """
    This function displays the main menu onto the console.

    Args:
        self (MainMenu) : the current  azs MainMenu object
    """
    def displayMenu(self):

        # Displaying main menu items
        print("1. Display Items\n"
              "2. Search Items\n"
              "3. Add or Remove Items\n"
              "4. Add or Remove Categories\n"
              "5. Edit Item Menu\n"
              "6. Logout\n")


    """
    This function updates the system object's state given the user's
    inputs to interact with the main menu.

    Args:
        self (MainMenu) : the current MainMenu object
        system (System) : the System object of interest
    """
    def update(self, system):

        # Loading all item and category data
        if not system.dataLoaded:
            system.itemdb.readData()
            system.catdb.readData()
            system.dataLoaded = True

        # Possible states
        states = {1: dim.DisplayItemsMenu, 2: si.SearchItems, 3: arim.AddRemoveItemMenu, 4: arcm.AddRemoveCategoryMenu, 5: eim.EditItemMenu, 6: logout.Logout}

        # Displaying header and welcome message
        ims_tools.newScreen()
        system.displayWelcomeMsg()
        print()

        # Displaying main menu and getting user input
        self.displayMenu()
        userInput = user_input.getIntRange("Enter your choice: ", 1, len(states) + 1)
        system.changeState(states[userInput]())