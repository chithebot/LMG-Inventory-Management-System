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
    for. If the user does not wish to search in this field, then
    None should be returned.

    Args:
        self (SearchItems) : the current SearchItems object
        system (System)    : the System object of interest
    
    Returns:
        Returns an string which is the item's name search
        parameter. None is returned if no search is desired.
    """
    def getName(self, system):
        
        # Getting user input from the user
        print("Enter the NAME of the item(s) you wish to search for.")
        print("Enter -1 to not search by NAME.")
        userInput = user_input.getString("Enter the item name: ", 1, NAME_MAX)
    
        # Checks if the user input is for not searching by name
        if (userInput.replace(' ', '') == NO_SEARCH_STR):
            return None
        return userInput


    """
    This function gets the user input on the item SKU to search
    for. If the user does not wish to search in this field,
    then None should be returned.

    Args:
        self (SearchItems) : the current SearchItems object
        system (System)    : the System object of interest
    
    Returns:
        Returns an integer which is the item's SKU search
        parameter. None is returned if no search is desired.
    """
    def getSKU(self, system):

        # Getting user input from the user
        print("Enter the SKU of the item(s) you wish to search for.")
        print("Enter -1 to not search by SKU.")
        userInput = user_input.getIntRange("Enter the item SKU: ", SKU_MIN_VALUE, SKU_MAX_VALUE + 1, [NO_SEARCH])
    
        # Checks if the user input is for not searching by SKU
        if userInput == NO_SEARCH:
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

        # Display categories
        ims_tools.displayCategories(["none"] + system.catdb.db, 0)

        # Asking user to choose an existing category to apply to the item
        print("Enter the entry number of the CATEGORY of the item(s) you wish to search for.\n"
              "Enter -1 to not search by CATEGORY.\n")
        userInput = user_input.getIntRange("Enter the category entry: ", -1, len(system.catdb) + 1)
        if userInput ==  NO_SEARCH:
            return None 
        elif userInput == 0:
            return "none"
        return system.catdb[userInput - 1]


    """
    This function gets the user input on the item quantity to
    search for. If the user does not wish to search in this
    field, then None should be returned.

    Args:
        self (SearchItems) : the current SearchItems object
        system (System)    : the System object of interest
    
    Returns:
        Returns an integer which is the item's quantity search
        parameter. None is returned if no search is desired.
    """
    def getQuantity(self, system):
        
        # Getting user input from the user
        print("Enter the QUANTITY of the item you wish to search for.")
        print("Enter -1 to not search by QUANTITY.")
        userInput = user_input.getIntRange("Enter the item quantity: ", -1, QUANTITY_MAX_VALUE + 1)
    
        # Checks if the user input is for not searching by SKU
        if userInput == NO_SEARCH:
            return None
        return userInput


    """
    This function searches a passed in database for items containing the passed
    in parameters. A list containing all the search results is returned.

    Args:
        self (SearchItems)                  : the current SearchItems object
        parameters (list<(string, string)>) : the parameter names and parameters
        db (list<Item>)                     : the database being searched

    Returns:
        Returns a list containing all the results of the search.
    """
    def search(self, parameters, db):

        # Check if there are parameters to search
        if not parameters:
            return db
        
        # Fills search results containing the search parameters
        results = []        # the search results
        for item in db:

            validItem = True        # indicates if item contains all valid parameters

            # Checking that item contains the parameter values
            for pair in parameters:

                paramName = pair[0]
                param = pair[1].lower()
                itemAttr = str(getattr(item, paramName)).replace(' ','').lower()
                
                # Checks if parameter is in current item
                if paramName in ['category', 'quantity']:
                    if param != itemAttr:
                        validItem = False
                else:
                    if param not in itemAttr:
                        validItem = False

            # Inserting item into search results if it contains all valid parameters
            if validItem:
                results.append(item)        
        return results

    """
    This function gets user input on the item information they would
    like to search in the database. All inputs containing the searched
    values will be present in the search results.

    Args:
        self (SearchItems) : the current SearchItems object
        system (System)    : the System object of interest
    """
    def update(self, system):        

        # Sorting item database
        system.itemdb.sortBySKU()
        
        # Function list definition
        funcList = [self.getName, self.getSKU, self.getCategory, self.getQuantity]   # contains functions for getting item information from user

        # Handling search functionality
        quit = False
        while not quit:

            # Search parameter definition
            searchParameterNames = ['name', 'sku', 'category', 'quantity']  # name and order of search parameters
            searchParameters = []                                           # search parameters

            for i in range(len(funcList)):
                
                # Preparing new screen getting search parameter from user
                ims_tools.newScreen()
                print("Items containing your search parameters will be shown in the search results.\n")
                parameter = funcList[i](system)
                
                # Inserting to search parameter list only if it is a valid parameter
                if parameter is not None:
                    searchParameters.append((searchParameterNames[i], str(parameter).strip()))

            # Searching item database for items containing the given information
            results = self.search(searchParameters, system.itemdb.db)     # contains search results

            # Preparing new screen then displaying search results
            ims_tools.newScreen()
            if results:
                self.displaySearchResults(results)
            else:
                print("No search results!\n")
            quit = (user_input.getYesOrNo("Would you like to search again?") == 'n')

        # Changing the system state to display items menu
        system.changeState(main_menu.MainMenu())