import change_password
import create_user
import exit
import ims_tools
import login
import menu
import state
import user_input


class StartMenu(menu.Menu, state.State):
    """ This class is the system object's state where the start menu is 
    displayed and the user interacts with to move to other system states.
    """

    """
    This function displays the start menu onto the console.

    Args:
        self (StartMenu) : the current StartMenu object
    """
    def displayMenu(self):

        # Displaying start menu items
        print("Welcome to the Inventory Management System.\n")
        print("1. Login\n"
              "2. Create an Account\n"
              "3. Forgot Password?\n"
              "4. Exit\n")


    """
    This function updates the system object's state given the user's
    inputs to interact with the start menu.

    Args:
        self (StartMenu) : the current StartMenu object
        system (System)  : the System object of interest
    """
    def update(self, system):
        
        # Defining possible states
        states = {1: login.Login, 2: create_user.CreateUser, 3: change_password.ChangePassword, 4: exit.Exit}

        # Displaying start menu
        ims_tools.newScreen()
        self.displayMenu()

        # Getting user decision and changing system state accordingly
        userInput = user_input.getIntRange("Enter your choice: ", 1, len(states) + 1)
        system.changeState(states[userInput]())