import copy

import edit_item_menu as eim
from ims_constants import *
import ims_tools
import state
import user_input


class ChangeItemQuantity(state.State):
    """ This class is the system object's change item  quantity state.
    The user chooses an item to change the quantity of, and the user
    chooses to increase or decrease the quantity by a valid amount.
    """

    """
    This function gets the user input on the item quantity to
    edit to and checks that the quantity is valid.

    Args:
        self (ChangeItemQuantity) : the current ChangeItemQuantity object
        item (Item)               : an Item object of interest
    
    Returns:
        Returns an integer which represents the amount to change
        the passed in item's quantity by
    """
    def getChangeInQuantity(self, item):
        
        # Getting user input from the user
        ims_tools.newScreen()
        ims_tools.displayItemInfo("Item information:", item)
        print("Enter the amount you wish to increase or decrease the item QUANTITY by.")
        return user_input.getIntRange("Enter the item quantity: ", -item.quantity, (QUANTITY_MAX_VALUE - item.quantity) + 1)


    """
    This function displays all items in the item database and
    gets user input on which item entry they would like to edit.
    The index of the item is returned.

    Args:
        self (ChangeItemQuantity) : the current ChangeItemQuantity object
        system (System)           : the System object of interest
    
    Returns:
        Returns the index of the item to be edited.
    """
    def getItemIndexToEdit(self, system):
        
        # Displaying the item data and getting user input on which item they would like to edit
        ims_tools.newScreen()
        system.displayAllItems()
        return user_input.getIntRange("Enter the entry number of the item you wish to edit: ", 1, len(system.itemdb) + 1) - 1


    """
    This function gets confirmation from the user if they would like to
    change the quantity of the passed in item. If the user confirms for a
    change then this function edits the item's quantity.

    Args:
        self (ChangeItemQuantity) : the current ChangeItemQuantity object
        system (System)           : the System object of interest
        itemIndex (int)           : the index of the Item object of interest
        change (int)              : the amount to change the Item quantity by
    """
    def confirmUserEdit(self, system, itemIndex, change):
        
        # Only changing item quantity if change is non-zero
        if change != 0:

            # Preparing new screen
            ims_tools.newScreen()

            # Displaying item before and after change
            item = system.itemdb[itemIndex]
            editedItem = copy.deepcopy(item)
            editedItem.quantity += change
            ims_tools.displayItemInfo("Item before change:", item)
            ims_tools.displayItemInfo("Item after change:", editedItem)
            
            # Generating prompt and getting confirmation from user if they would like to change the quantity
            confirm = (user_input.getYesOrNo("Would you like to go through with the change?") == 'y')

            # Changing item quantity
            if confirm:

                # Increasing the item quantity
                item.quantity += change

                # Setting system's item change flag to on
                if not system.itemChange:
                    system.itemChange = True


    """
    This function gets user input on the item to edit and edits
    the item attributes which the user desires to change.

    Args:
        self (ChangeItemQuantity) : the current ChangeItemQuantity object
        system (System)           : the System object of interest
    """
    def update(self, system):        

        # Sorting item database
        system.itemdb.sortBySKU()

        # Handling edit item functionality
        quit = False
        while not quit:

            # Displaying the item data and getting user input on which item they would like to edit
            itemIndex = self.getItemIndexToEdit(system)

            # Getting quantity to increase quantity of item by
            change = self.getChangeInQuantity(system.itemdb[itemIndex])

            # Only changing item quantity if change is non-zero
            self.confirmUserEdit(system, itemIndex, change)
            quit = (user_input.getYesOrNo("Would you like to edit another item?") == 'n')

        # Changing the system state to display items menu
        system.changeState(eim.EditItemMenu())