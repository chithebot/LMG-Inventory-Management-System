import category_database as cdb
import datetime
from ims_constants import *
import ims_tools
import introduction
import item_database as idb
import user
import user_database as udb


class System:

    """ This class is the controller which handles facilitating interactions between
    boundary objects, entity objects, and users.

        Attributes:
            _catdb (CategoryDatabase) : the category database
            _itemdb (ItemDatabase)    : the item database
            _userdb (UserDatabase)    : the user database
            _user (User)              : the logged in user of the system
            _state (State)            : the state of the system
            _loaded (bool)            : the loaded status of the system's item and category data
            _categoryChange (bool)    : the change status in the system category data
            _itemChange (bool)        : the change status in the system item
            _exit (bool)              : the exit status of the system
    """

    """
    This function initializes a System object.

    Args:
        self (System)     : the current System object
    """
    def __init__(self, filename_cdb, filename_idb, filename_udb):

        # Initializing System attributes
        self._catdb = cdb.CategoryDatabase(filename_cdb)    # contains the category database
        self._itemdb = idb.ItemDatabase(filename_idb)       # contains the item database
        self._userdb = udb.UserDatabase(filename_udb)       # contains the user database
        self._user = user.User()                            # current user of the system
        self._state = introduction.Introduction()           # state of the current system
        self._dataLoaded = False                            # indicates if the system has already loaded item and category data
        self._userLoaded = False                            # indicates if the system has already loaded user data
        self._categoryChange = False                        # indicates if a changes have been made to the catdb
        self._itemChange = False                            # indicates if a changes have been made to the itemdb
        self._exit = False                                  # indicates exit status of system


    """
    This function gets the current System object's category database.

    Args:
        self (System) : the current System object

    Returns:
        Returns the System object's category database.
    """
    @property
    def catdb(self):
        return self._catdb


    """
    This function gets the current System object's item database.

    Args:
        self (System) : the current System object

    Returns:
        Returns the System object's item database.
    """
    @property
    def itemdb(self):
        return self._itemdb


    """
    This function gets the current System object's user database.

    Args:
        self (System) : the current System object

    Returns:
        Returns the System object's user database.
    """
    @property
    def userdb(self):
        return self._userdb


    """
    This function gets the current System object's authorized user.

    Args:
        self (System) : the current System object

    Returns:
        Returns the System object's current authorized user.
    """
    @property
    def user(self):
        return self._user


    """
    This function gets the current System object's item and category data
    loaded status. This status indicates if the System object's item or
    category database were loaded.

    Args:
        self (System) : the current System object

    Returns:
        Returns the System object's item and category loaded status.
    """
    @property
    def dataLoaded(self):
        return self._dataLoaded  


    """
    This function gets the current System object's user data loaded
    status. This status indicates if the System object's user data were
    loaded.

    Args:
        self (System) : the current System object

    Returns:
        Returns the System object's user data loaded status.
    """
    @property
    def userLoaded(self):
        return self._userLoaded  


    """
    This function gets the current System object's change status. This
    status indicates if the System object's category database was changed.

    Args:
        self (System) : the current System object

    Returns:
        Returns the System object's category change status.
    """
    @property
    def categoryChange(self):
        return self._categoryChange


    """
    This function gets the current System object's item change status. This
    status indicates if the System object's item database was changed.

    Args:
        self (System) : the current System object

    Returns:
        Returns the System object's item change status.
    """
    @property
    def itemChange(self):
        return self._itemChange


    """
    This function gets the current System object's exit status. This
    status indicates if the System object should terminate.

    Args:
        self (System) : the current System object

    Returns:
        Returns the System object's exit status.
    """
    @property
    def exit(self):
        return self._exit


    """
    This function displays a welcome message to the user.

    Args:
        self (System) : the current System object
    """
    def displayWelcomeMsg(self):
        
        # Getting current time
        currentTime = datetime.datetime.now().hour

        # Displaying welcome message
        welcomeString = ""
        if 6 <= currentTime < 12:
            welcomeString += "Good Morning"
        elif 12 <= currentTime < 18:
            welcomeString += "Good Afternoon"
        else:
            welcomeString += "Good Evening"

        # Adding user's name to welcome message if user has name
        if len(self.user.name) > 0:
            welcomeString += f", {self.user.name}"
        welcomeString += "!"
        print(welcomeString)


    """
    This function displays all items in the item database.

    Args:
        self (System) : the current System object
    """
    def displayAllItems(self):

        ims_tools.displayItems(self.itemdb)

    """
    This function displays items, in the item database, that belong
    to the specified category.

    Args:
        self (System)       : the current System object
        category (Category) : the category to display
    
    Raises:
        NameError : Raised if passed in category does not exist in
                    category database.
    """
    def displayItemsInCategory(self, category):

        # Raises an exception if category is not valid
        if category not in self.catdb.db:
            raise NameError(f"'{category}' is not a valid category.")
        
        # Displaying all items in category
        ims_tools.displayItems([item for item in self.itemdb if item.category == category])


    """
    This function displays all categories in the category database.

    Args:
        self (System) : the current System object
    """
    def displayCategories(self):
        ims_tools.displayCategories(self.catdb)
        

    """
    This function sets the current System object's item and
    category data loaded status to the passed in status.

    Args:
        self (System)     : the current System object
        dataLoaded (bool) : the loaded status to set
    """
    @dataLoaded.setter
    def dataLoaded(self, dataLoaded):
        self._dataLoaded = dataLoaded



    """
    This function sets the current System object's user data
    loaded status to the passed in status.

    Args:
        self (System)     : the current System object
        userLoaded (bool) : the loaded status to set
    """
    @userLoaded.setter
    def userLoaded(self, userLoaded):
        self._userLoaded = userLoaded


    """
    This function sets the current System object's category change
    status to the passed in status.

    Args:
        self (System)         : the current System object
        categoryChange (bool) : the category change status to set
    """
    @categoryChange.setter
    def categoryChange(self, categoryChange):
        self._categoryChange = categoryChange


    """
    This function sets the current System object's item change status
    to the passed in status.

    Args:
        self (System)     : the current System object
        itemChange (bool) : the item change status to set
    """
    @itemChange.setter
    def itemChange(self, itemChange):
        self._itemChange = itemChange


    """
    This function sets the current System object's exit status
    to the passed in exit status.

    Args:
        self (System) : the current System object
        exit (bool)   : the exit status to set
    """
    @exit.setter
    def exit(self, exit):
        self._exit = exit


    """
    This function resets the current System object's change and loaded status
    to their default values, False.

    Args:
        self (System) : the current System object
    """  
    def resetStatus(self):
        self.loaded = False
        self.change = False


    """
    This function clears the current user's data from the system. 

    Args:
        self (System) : the current System object
    """
    def clearCurrentUser(self):
        self.user.clear()

 
    """
    This function changes the state of the System object to the given
    state.

    Args:
        self (System) : the current System object
    """
    def changeState(self, state):
        self._state = state


    """
    This function updates the current System object, in accordance,
    to its current state.

    Args:
        self (System) : the current System object
    """
    def update(self):
        self._state.update(self)