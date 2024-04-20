import add_remove_item_menu as arim
from ims_constants import *
import ims_tools
import state
import user_input


class RemoveItem(state.State):
    """ This class is the system object's remove item state. In this state,
    the user is given the ability to remove an item from the database. 
    """

    """
    This function updates the system object's database by removing an item,
    inputted by the user, from the item database if it is not yet in there.

    Args:
        self (RemoveItem) : the current RemoveItem object
        system (System)   : the System object of interest
    """
    def update(self, system):
        
        # Sorting items by SKU
        system.itemdb.sortBySKU()

        # Getting item data from user
        quit = False
        while not quit:

            # Returns user back to menu if item database is empty
            if system.itemdb.empty():
                quit = True
                print("No items to remove!")
                user_input.getContinue("Press ENTER to continue.")
                continue

            # Variable definitions
            removeDict = {}
            userInput = -1

            # Asking user which items they would like to remove
            while userInput != 0:
                
                # Preparing new screen and displaying items
                ims_tools.newScreen()
                system.displayAllItems()

                # Displaying entries up for removal
                print("Entries up for removal:")
                for i, entry in enumerate(removeDict.keys()):
                    if i % 10 == 0:
                        print()
                    print(entry, end=' ')
                print('\n')

                # Prompting user to enter the entry number of the items
                print("Enter the entry you wish to remove. Enter the value, 0, once you are done.")
                userInput = user_input.getIntRange("Enter the entry number: ", 0, len(system.itemdb) + 1)

                # Adding user input to remove dictionary 
                if userInput != 0:
                    removeDict[userInput] = None

            
            # Asking user for confirmation on whether to remove the item
            confirm = (user_input.getYesOrNo("Are you sure you want to remove this item?") == 'y')
            
            # Only attempting to remove the item if user confirmed it
            if confirm:

                    # Removing item(s) from database
                    removeList = list(removeDict.keys())
                    removeList.sort(reverse=True)
                    for entry in removeList:
                        system.itemdb.pop(entry - 1)

                    # Set system's item change flag to on
                    if not system.itemChange and len(removeList) > 0:
                        system.itemChange = True

                    # Preparing new screen and displaying all items
                    ims_tools.newScreen()
                    system.displayAllItems()

            # Only asks the user if they wants to remove more items if there are items in database
            if not system.itemdb.empty():
                quit = (user_input.getYesOrNo("Would you like to remove more items?") == 'n')

        # Changing system state back to the add/remove category menu
        system.changeState(arim.AddRemoveItemMenu())