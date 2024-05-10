import display_items_menu as dim
from ims_constants import *
import ims_tools
import state
import user_input


class DisplayItemsAll(state.State):
    """ This class is the system object's state where the system displays
    all items in its database.
    """

    """
    This function displays the attributes in which the database can
    sort the items by, in item database.

    Args:
        self (DisplayItemsAll) : the current DisplayItemsAll object
    """
    def displaySortChoices(self):
        
        # Displaying sort choice menu
        print("1. Name\n"
              "2. SKU\n"
              "3. Category\n"
              "4. Quantity\n"
              "5. Quit\n")


    """
    This function displays the ordering in which the database can sort
    the items by. 

    Args:
        self (DisplayItemsAll) : the current DisplayItemsAll object
    """
    def displayOrderingChoices(self):
        
        # Displaying ordering menu
        print("1. Ascending (A-Z; 0-9)\n"
              "2. Descending (Z-A; 9-0)\n")


    """
    This function gets user input on whether to display in lexicographical
    or reverse lexicographical order then display the items. The system object's
    state is changed to the display items menu.

    Args:
        self (DisplayItemsAll) : the current DisplayItemsAll object
        system (System)        : the System object of interest
    """
    def update(self, system):        
        
        # Sorting function dictionary and parameter dictionary definitions
        sortType = {SORT_NAME: system.itemdb.sortByName,
                    SORT_SKU: system.itemdb.sortBySKU,
                    SORT_CATEGORY: system.itemdb.sortByCategory,
                    SORT_QUANTITY: system.itemdb.sortByQuantity}
        reverseParam = {ASCENDING: False, DESCENDING: True}

        # Displaying IMS header
        ims_tools.newScreen()

        # Displaying data onto screen
        userInput = SORT_SKU           # auto-setting to display in ascending SKU order
        order = ASCENDING
        while userInput != QUIT_DISPLAY_ALL:

            # Sorting items database
            sortType[userInput](reverseParam[order])

            # Preparing new screen, and displaying header and all items
            ims_tools.newScreen()
            system.displayAllItems()

            # Prompting user to choose sort type
            print("Sort the items by:")
            self.displaySortChoices()
            userInput = user_input.getIntRange("Enter your choice: ", 1, 6)
            print()

            # Prompting user for order type
            if userInput != QUIT_DISPLAY_ALL:
                print("Order the items in:")
                self.displayOrderingChoices()
                order = user_input.getIntRange("Enter your choice: ", 1 , 3)
                print()

        # Changing the system state to display items menu
        system.changeState(dim.DisplayItemsMenu())