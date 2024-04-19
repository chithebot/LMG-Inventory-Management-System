from ims_constants import *
import ims_tools
import main_menu
import state
import user_input


class SearchItems(state.State):
    """ This class is the system object's state where the user can search
    for item by its name in the database.
    """

    """
    This function displays all item data in the passed in search
    result list.

    Args:
        self (SearchItems)   : the current SearchItems object
        results (list<Item>) : the list of search results
    """
    def displaySearchResults(self, results):
        ims_tools.displayItems(results)


    """
    This function gets the user input on the item name to search
    for. If the user does not wish to search in this field,
    then None should be returned.

    Args:
        self (SearchItems) : the current SearchItems object
    
    Returns:
        Returns an string which is the item's name search
        parameter. None is returned if no search is desired.
    """
    def getName(self):
        
        # Getting user input from the user
        print("Enter the NAME of the item you wish to search for.")
        print("Leave the field blank to not search by NAME.")
        userInput = user_input.getString("Enter the item name:", 0, NAME_MAX)
    
        # Checks if the user input is for not searching by name
        if (len(userInput.replace(' ', '')) == 0):
            return None
        return userInput


    """
    This function gets the user input on the item SKU to search
    for. If the user does not wish to search in this field,
    then None should be returned.

    Args:
        self (SearchItems) : the current SearchItems object
    
    Returns:
        Returns an integer which is the item's SKU search
        parameter. None is returned if no search is desired.
    """
    def getSKU(self):

        # Getting user input from the user
        print("Enter the SKU of the item you wish to search for.")
        print("Enter -1 to not search by SKU.")
        userInput = user_input.getIntRange("Enter the item SKU:", -1, SKU_MAX_VALUE + 1)
    
        # Checks if the user input is for not searching by SKU
        if userInput == -1:
            return None
        return userInput


    """
    This function gets the user input on the item category to
    search for. If the user does not wish to search in this field,
    then None should be returned.

    Args:
        self (SearchItems) : the current SearchItems object
        system (System)    : the System object of interest

    Returns:
        Returns an integer which is the item's category search
        parameter. None is returned if no search is desired.
    """
    def getCategory(self, system):

        # display categories
        # have user pick from categories
        pass


    """
    This function gets the user input on the item quantity to
    search for. If the user does not wish to search in this
    field, then None should be returned.

    Args:
        self (SearchItems) : the current SearchItems object
    
    Returns:
        Returns an integer which is the item's quantity search
        parameter. None is returned if no search is desired.
    """
    def getQuantity(self):
        
        # Getting user input from the user
        print("Enter the QUANTITY of the item you wish to search for.")
        print("Enter -1 to not search by QUANTITY.")
        userInput = user_input.getIntRange("Enter the item quantity:", -1, QUANTITY_MAX_VALUE + 1)
    
        # Checks if the user input is for not searching by SKU
        if userInput == -1:
            return None
        return userInput


    """
    This function gets user input on the item information they would
    like to search in the database. All inputs containing the searched
    values will be present in the search results.

    Args:
        self (SearchItems) : the current SearchItems object
        system (System)    : the System object of interest
    """
    def update(self, system):        

        # Function list definition
        funcList = {}   # contains functions for getting item information from user

        # Handling search functionality
        quit = False
        while not quit:

            # Search parameter definition (order is [name, sku, category, quantity])
            searchParameters = [None, None, None, None]

            for i in range(len(funcList)):
                
                # Preparing new screen getting search parameter from user
                ims_tools.newScreen()
                print("Items containing your search parameters will be shown in the search results.\n")
                if i == 3:
                    searchParameters[i] = funcList[i](system)
                searchParameters[i] = funcList[i]()

            # Searching item database for items containing the given information
            results = []                                    # contains search results


            # Preparing new screen then displaying search results
            ims_tools.newScreen()
            if results:
                self.displaySearchResults()
            else:
                print("No search results!\n")

        # Changing the system state to display items menu
        system.changeState(main_menu.MainMenu)