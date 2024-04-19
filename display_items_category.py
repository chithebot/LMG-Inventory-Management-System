import display_items_menu as dim
import ims_tools
import state
import user_input


class DisplayItemsCategory(state.State):
    """ This class is the system object's state where the system displays
    items in a specific category.
    """

    """
    This function gets user input on which category of items to display,
    and the items are displayed. The system object's state is changed to
    the display items menu.

    Args:
        self (DisplayItemsCategory) : the current DisplayItemsCategory object
        system (System)             : the System object of interest
    """
    def displayChoices(self, system):

        # Displaying categories onto console
        print("Pick a category of items to display.")
        for index, cat in enumerate(system.catdb.db):
            print(f"{index + 1}. {cat}")
        print()


    """
    This function gets user input on which category of items to display,
    and the items are displayed. The system object's state is changed to
    the display items menu.

    Args:
        self (DisplayItemsCategory) : the current DisplayItemsCategory object
        system (System)             : the System object of interest
    """
    def update(self, system):

        # Getting category of items user wants to display and displaying them
        userInput = 'y'
        while userInput == 'y':

            # Preparing new screen, and display existing categories and get user input on which category of items to display
            ims_tools.newScreen()
            self.displayChoices(system)
            choice = user_input.getIntRange("Enter the category you would like to display: ", 1, len(system.catdb) + 1)
        
            # Displaying items in a new screen
            ims_tools.newScreen()
            system.displayItemsInCategory(system.catdb[choice - 1])

            # Prompting user to press any key to continue
            userInput = user_input.getYesOrNo("Display another category?")

        # Changing the system state to display items menu
        system.changeState(dim.DisplayItemsMenu())