import copy

import edit_item_menu as eim
from ims_constants import *
import ims_tools
import state
import user_input


class EditItem(state.State):
    """ This class is the system object's edit item state. The user
    chooses an item to edit and edits its attributes. 
    """

    """
    This function gets the user input on the item name to edit
    the passed in item's name to. The user can also choose not
    to edit this field.

    Args:
        self (EditItem) : the current EditItem object
        system (System) : the System object of interest
        item (Item)     : an Item object of interest
    """
    def editName(self, system, item):
        
        # Getting user input from the user
        print("Enter the NAME you wish to edit to.")
        print("Enter -1 to not edit the NAME.")
        userInput = user_input.getString("Enter the item name: ", 1, NAME_MAX)
    
        # Getting new item name if previous entry already exists
        same = userInput.replace(' ','').lower() == item.name.replace(' ', '').lower()
        while userInput != NO_EDIT_STR and not same and ims_tools.nameExistIn(userInput, system.itemdb.db):
            print(f"'{userInput}' already exists within the database. Please enter another item name.\n")
            userInput = user_input.getString("Enter the item name: ", 1, NAME_MAX)
            same = userInput.replace(' ','').lower() == item.name.replace(' ', '').lower()

        # Editing item name
        if userInput != NO_EDIT_STR and not same:
            item.name = userInput


    """
    This function gets the user input on the item SKU to edit
    the passed in item's SKU to. The user can also choose not
    to edit this field.

    Args:
        self (EditItem) : the current EditItem object
        system (System) : the System object of interest
        item (Item)     : an Item object of interest
    """
    def editSKU(self, system, item):

        # Getting user input from the user
        print("Enter the SKU you wish to edit to.")
        print("Enter -1 to not edit the SKU.")
        userInput = user_input.getIntRange("Enter the item SKU: ", SKU_MIN_VALUE, SKU_MAX_VALUE + 1, [NO_EDIT])
    
        # Getting new item SKU if previous entry already exists
        same = userInput == item.sku
        while userInput != NO_EDIT and not same and ims_tools.SKUExistIn(userInput, system.itemdb.db):
            print(f"'{userInput}' already exists within the database. Please enter another item SKU.")
            userInput = user_input.getIntRange("Enter the item SKU: ", SKU_MIN_VALUE, SKU_MAX_VALUE + 1, [NO_EDIT])
            same = userInput == item.sku
        
        # Editing item SKU
        if userInput != NO_EDIT and not same:
            item.sku = userInput

 
    """
    This function gets the user input on the item category to
    edit the passed in item's category to. The user can also
    choose not to edit this field.

    Args:
        self (EditItem) : the current EditItem object
        system (System) : the System object of interest
        item (Item)     : an Item object of interest
    """
    def editCategory(self, system, item):

        # Display categories
        ims_tools.displayCategories(["none"] + system.catdb.db, 0)

        # Asking user to choose an existing category to apply to the item
        print("Enter the entry number of the CATEGORY you wish to edit to.\n"
              "Enter -1 to not edit the CATEGORY.\n")
        userInput = user_input.getIntRange("Enter the category entry: ", -1, len(system.catdb) + 1)
        if userInput == 0:
            item.category = "none"
        elif userInput > 0:
            item.category = system.catdb[userInput - 1]


    """
    This function gets the user input on the item quantity to
    to edit the passed in item's quantity to. The user can also
    choose not to edit this field.

    Args:
        self (EditItem) : the current EditItem object
        system (System) : the System object of interest
        item (Item)     : an Item object of interest
    """
    def editQuantity(self, system, item):
        
        # Getting user input from the user
        print("Enter the QUANTITY of the item you wish to edit to.")
        print("Enter -1 to not edit the QUANTITY.")
        userInput = user_input.getIntRange("Enter the item quantity: ", -1, QUANTITY_MAX_VALUE + 1)
    
        # Checks if the user input is for not searching by SKU
        if userInput != NO_EDIT:
            item.quantity = userInput


    """
    This function displays all items in the item database and
    gets user input on which item entry they would like to edit.
    The index of the item is returned.

    Args:
        self (EditItem) : the current EditItem object
        system (System) : the System object of interest
    
    Returns:
        Returns the index of the item to be edited.
    """
    def getItemIndexToEdit(self, system):
        
        # Displaying the item data and getting user input on which item they would like to edit
        ims_tools.newScreen()
        system.displayAllItems()
        return user_input.getIntRange("Enter the entry number of the item you wish to edit: ", 1, len(system.itemdb) + 1) - 1


    """
    This function gets the attributes, of the item, which the user
    desires to edit. It edits a copy of the passed in item and
    returns it.

    Args:
        self (EditItem) : the current EditItem object
        system (System) : the System object of interest

    Returns:
        Returns a copy of the passed in item object with the edits
        made.
    """
    def getAttributesToEdit(self, system, item):

        editedItem = copy.deepcopy(item)

        # Function list definition
        functionList = [self.editName, self.editSKU, self.editCategory, self.editQuantity]  # contains functions to get user input and edit items
        
        # Handles getting attributes to edit from user
        for i in range(len(functionList)):
                
            # Preparing new screen and getting edit arguments from user
            ims_tools.newScreen()
            ims_tools.displayItemInfo("Edited item:", editedItem)
            functionList[i](system, editedItem)
        return editedItem


    """
    This function gets confirmation from the user if they would like to
    edit the passed in item with the passed in edited item's attributes.
    If the user confirms for a change then this function edits the item.

    Args:
        self (EditItem)   : the current ChangeItemQuantity object
        system (System)   : the System object of interest
        itemIndex (int)   : the index of the Item object of interest
        editedItem (Item) : the Item object containing all edits
    """
    def confirmUserEdit(self, system, itemIndex, editedItem):
        
        # Only edits item if edited items are not the same
        if system.itemdb[itemIndex] != editedItem:

            # Confirms if user wants to keep the edits they made and edits the item
            ims_tools.newScreen()
            ims_tools.displayItemInfo("Edited item:", editedItem)
            confirm = (user_input.getYesOrNo("Would you like to keep the current edits on the item?") == 'y')
            if confirm:

                # Editing the item and sorting the list
                system.itemdb[itemIndex] = editedItem
                system.itemdb.sortBySKU()

                # Setting system's item change flag to on
                if not system.itemChange:
                    system.itemChange = True


    """
    This function gets user input on the item to edit and edits
    the item attributes which the user desires to change.

    Args:
        self (EditItem) : the current EditItem object
        system (System) : the System object of interest
    """
    def update(self, system):        

        # Sorting item database
        system.itemdb.sortBySKU()

        # Handling edit item functionality
        quit = False
        while not quit:

            # Displaying the item data and getting user input on which item they would like to edit
            itemIndex = self.getItemIndexToEdit(system)

            # Handles getting attributes to edit from user
            editedItem = self.getAttributesToEdit(system, system.itemdb[itemIndex])

            # Confirms if user wants to keep the edits they made and edits the item
            self.confirmUserEdit(system, itemIndex, editedItem)
            quit = (user_input.getYesOrNo("Would you like to edit another item?") == 'n')

        # Changing the system state to display items menu
        system.changeState(eim.EditItemMenu())