import bisect

import add_remove_category_menu as arcm
from ims_constants import *
import ims_tools
import state
import user_input


class AddCategory(state.State):
    """ This class is the system object's add category state. The user
    inputs a category to add to the category database. 
    """

    """
    This function updates the system object's database by adding a category,
    inputted by the user, into the category database if it is not yet in there.

    Args:
        self (AddCategory) : the current AddCategory object
        system (System)    : the System object of interest
    """
    def update(self, system):

        # Getting category from user or until they want to quit
        quit = False
        while not quit:
            
            # Preparing new screen and displaying all existing categories
            ims_tools.newScreen()
            system.displayCategories()
            print()

            # Getting user input on what category to add
            print("Please enter a category that does not yet exist above.")
            userInput = user_input.getString("Enter a category: ", min=1, max=CATEGORY_MAX)
            confirm = (user_input.getYesOrNo("Are you sure you want to add this category?") == 'y')
            
            # Only attempting to add the category if user confirmed it
            if confirm:

                try:
                    # Checking if category exist in database
                    system.catdb.index(userInput.lower())
                    print(f"\n'{userInput}' already exists within the database!")

                # Handles adding category into the database
                except ValueError:
                    
                    # Adding category to database
                    bisect.insort(system.catdb.db, userInput.lower())

                    # Setting system's category change flag to on
                    if not system.categoryChange:
                        system.categoryChange = True
                    
                    # Preparing new screen and displaying header
                    ims_tools.newScreen()
                    system.displayCategories()

            quit = (user_input.getYesOrNo("Would you like to add another category") == 'n')

        # Changing system state back to the add/remove category menu
        system.changeState(arcm.AddRemoveCategoryMenu())