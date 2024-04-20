import add_remove_category_menu as arcm
from ims_constants import *
import ims_tools
import state
import user_input


class RemoveCategory(state.State):
    """ This class is the system object's remove category state. The user
    inputs a category to remove from the category database. 
    """


    """
    This function updates the items, of the system's database, containing
    a certain category. It updates all their categories to the passed in
    category.

    Args:
        self (RemoveCategory) : the current RemoveCategory object
        system (System)       : the System object of interest
        removed (string)      : the removed category
        new (string)          : the replacement category
    """
    def replaceCategoriesAll(self, system, removed, new):
        
        # Setting categories of items, with the removed category, to none
        for i in range(len(system.itemdb)):
                    
            # Converting items with popped category to 'none' category
            item = system.itemdb[i]             # creating shallow copy                    
            if item.category == removed:
                        
                # Setting item category to none and set itemChanged status
                if not system.itemChange:
                    system.itemChange = True
                item.category = new

    """
    This function updates the system object's database by removing a category,
    inputted by the user, from the category database. It also updates the items,
    with the removed category tag, with a default category tag, 'none.'

    Args:
        self (RemoveCategory) : the current RemoveCategory object
        system (System)       : the System object of interest
    """
    def update(self, system):

        # Getting category from user or until they want to quit
        quit = False
        while not quit:

            # Returns user back to menu if category database is empty
            if system.catdb.empty():
                quit = True
                print("No categories to remove!")
                user_input.getContinue("Press ENTER to continue.")
                continue

            # Clearing screen, and displaying header and all existing categories
            ims_tools.newScreen()
            system.displayCategories()
            print()

            # Getting user input on what category to add
            print("Please enter a category to be removed.")
            userInput = user_input.getIntRange("Enter the entry number of the category to remove: ", 1, len(system.catdb) + 1)
            confirm = (user_input.getYesOrNo("Are you sure you want to remove this category?") == 'y')
            
            # Removing the category from the database and changing items with removed category to 'none'
            if confirm:

                # Clearing screen and displaying header
                ims_tools.newScreen()

                # Removing category from category database
                popped = system.catdb.pop(userInput - 1)

                # Setting system's category change flag to on
                if not system.categoryChange:
                    system.categoryChange = True
                print(f"\n'{popped}' was removed!\n")                

                # Displaying all categories
                system.displayCategories()
                print()
                user_input.getContinue("Press enter to continue.\n")

                # Setting categories of items, with the removed category, to 'none'
                self.replaceCategoriesAll(system, popped, "none")

                # Preparing new screen
                ims_tools.newScreen()
                print(f"Categories of items with the category, '{popped},' were set to 'none.'\n")

                # Sorting and displaying all items after categories were changed
                system.itemdb.sortByCategory()
                system.displayAllItems()
                print()

            if not system.catdb.empty():
                quit = (user_input.getYesOrNo("Would you like to remove another category") == 'n')

        # Changing system state back to the add/remove category menu
        system.changeState(arcm.AddRemoveCategoryMenu())