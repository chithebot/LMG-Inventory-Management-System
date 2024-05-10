import bisect

import add_remove_item_menu as arim
from ims_constants import *
import ims_tools
import item
import state
import user_input


class AddItem(state.State):
    """ This class is the system object's add item state. The user
    inputs an item and its information to add it to the item database. 
    """

    """
    This function clears the screen, displays all items in the database, and displays
    the new item information to be added.

    Args:
        self (AddItem)  : the current AddItem object
        system (System) : the System object which the database exists in
        header (string) : the header for the item being displayed
        item (Item)     : the Item object of to be displayed
    """
    def displayInfo(self, system, header, item):

        # Preparing new screen
        ims_tools.newScreen()
        system.displayAllItems()

        # Displaying new item
        ims_tools.displayItemInfo(header, item)

    
    """
    This function gets the name of the item being added, from the user, and
    returns it. It handles checking if the item name already exists within
    the system database and asks the user until a valid item name is entered. 

    Args:
        self (AddItem)  : the current AddItem object
        system (System) : the System object which the database exists in
    
    Returns:
        Returns a string which is the name of the item to be added.
    """
    def getItemName(self, system):

        # Getting item name and checking if it already exists in the item database
        userInput = user_input.getString("Enter the item name: ", 1, NAME_MAX)

        # Getting new item name if previous entry already exists
        while ims_tools.nameExistIn(userInput, system.itemdb.db):
            print(f"'{userInput}' already exists within the database. Please enter another item name.\n")
            userInput = user_input.getString("Enter the item name: ", 1, NAME_MAX)
        return userInput


    """
    This function gets the SKU of the item being added, from the user, and
    returns it. It handles checking if the item SKU already exists within
    the system database and asks the user until a valid item SKU is entered. 

    Args:
        self (AddItem)  : the current AddItem object
        system (System) : the System object which the database exists in
    
    Returns:
        Returns an integer  which is the SKU of the item to be added.
    """
    def getItemSKU(self, system):

        # Getting item SKU and checking if it already exists in the item database
        userInput = user_input.getIntRange("Enter the item SKU: ", SKU_MIN_VALUE, SKU_MAX_VALUE + 1)
        
        # Getting new item SKU if previous entry already exists
        if ims_tools.SKUExistIn(userInput, system.itemdb.db):
            print(f"'{userInput}' already exists within the database. Please enter another item SKU.")
            userInput = user_input.getIntRange("Enter the item SKU: ", SKU_MIN_VALUE, SKU_MAX_VALUE + 1)
        return userInput

    
    """
    This function gets the category of the item being added, from the user,
    and returns it. The categories are chosen from a list of already existing
    categories.

    Args:
        self (AddItem)  : the current AddItem object
        system (System) : the System object which the database exists in
    
    Returns:
        Returns a string which is the category of the item to be added.
    """
    def getCategory(self, system):

        # Displaying all categories
        system.displayCategories()

        # Asking user to choose an existing category to apply to the item
        print("Choose a category to apply to the new item.\n"
              "If you do not want to enter a category, ENTER '0'.")
        userInput = user_input.getIntRange("Enter the category entry: ", 0, len(system.catdb) + 1)
        if userInput != 0:
            return system.catdb[userInput - 1]
        return "none"


    """
    This function gets the quantity to be assigned to the new item being added,
    from the user, and returns it.

    Args:
        self (AddItem)  : the current AddItem object
        system (System) : the System object which the database exists in
    
    Returns:
        Returns an integer which represents the quantity of the new item.
    """
    def getQuantity(self, system):
        return user_input.getIntRange("Enter the initial item quantity: ",
                                      QUANTITY_MIN_VALUE, QUANTITY_MAX_VALUE + 1)


    """
    This function updates the system object's database by adding an item,
    inputted by the user, into the item database if it is not yet in there.

    Args:
        self (AddItem)  : the current AddItem object
        system (System) : the System object of interest
    """
    def update(self, system):
    
        # Function and attribute dictionary
        funcList = [self.getItemName, self.getCategory, self.getItemSKU, self.getQuantity]  # function list for getting item info
        attrList = ["name", "category", "sku", "quantity"]                                  # attribute list for item

        # Sorting items by SKU
        system.itemdb.sortBySKU()

        # Getting item data from user
        quit = False
        while not quit:

            # Preparing item to be added and data to be scanned
            newItem = item.Item()                   # contains the new item to be added
            
            # Getting information on new item to be added
            for i in range(len(funcList)):
                
                # Preparing new screen, displaying all items, and displaying new item information
                self.displayInfo(system, "New Item Information:", newItem)

                # Getting information on item and assigning that information to the new item
                info = funcList[i](system)

                # Setting user input to appropriate Item attribute
                setattr(newItem, attrList[i], info)

            # Asking user for confirmation on whether to add new item 
            confirm = (user_input.getYesOrNo("Are you sure you want to add this item?") == 'y')
            
            # Only attempting to add the item if user confirmed it
            if confirm:
                
                # Adding new item into database
                bisect.insort(system.itemdb.db, newItem)

                # Set system's item change flag to on
                if not system.itemChange:
                    system.itemChange = True

                # Preparing new screen and sorting items by SKU
                ims_tools.newScreen()

                # Displaying items
                system.displayAllItems()

            quit = (user_input.getYesOrNo("Would you like to add another item?") == 'n')

        # Changing system state back to the add/remove category menu
        system.changeState(arim.AddRemoveItemMenu())