import change_item_quantity as ciq
import edit_item
import ims_tools
import main_menu
import menu
import state
import user_input


class EditItemMenu(menu.Menu, state.State):
    """ This class is the system object's edit item state.
    The user can chooses if they would like to increase or decrease
    the quantity of an existing item, or just edit the details of an
    existing item.
    """

    """
    This function displays the edit item menu onto the console.

    Args:
        self (EditItemMenu) : the current EditItemMenu object
    """
    def displayMenu(self):

        # Displaying add/remove item menu items
        print("1. Increase/Decrease Item Quantity\n"
              "2. Edit Item\n"
              "3. Back\n")


    """
    This function updates the system object's state by displaying the edit
    item menu and changes the system state according to which action
    the user decides to take.

    Args:
        self (EditItemMenu) : the current EditItemMenu object
        system (System)     : the System object of interest
    """
    def update(self, system):

        # Possible states
        states = {1: ciq.ChangeItemQuantity, 2: edit_item.EditItem, 3: main_menu.MainMenu}

        # Displaying edit item menu and getting user input
        ims_tools.newScreen()
        self.displayMenu()
        userInput = user_input.getIntRange("Enter your choice: ", 1, len(states) + 1)
        system.changeState(states[userInput]())