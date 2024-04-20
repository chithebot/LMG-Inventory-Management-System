import ims_tools
from ims_constants import *
import main_menu
import start_menu
import state
import user_input


class CreateUser(state.State):
    """ This class is the system object's create user state which a
    user interacts with to create an account to access more system
    features.
    """

    """
    This function handles creating a user account and then logging them
    in with the newly created account. 

    Args:
        self (CreateUser) : the current CreateUser object
        system (System)   : the System object of interest
    """
    def update(self, system):

        # Possible states for the system to update to
        states = {1: start_menu.StartMenu, 2: main_menu.MainMenu}

        # Read user data into the system user database
        system.userdb.readData()
        
        # Displaying application header and introduction message
        ims_tools.newScreen()
        print("Welcome new user! Enter your desired username to get started!")
        print(f"The username must have at least {USERNAME_MIN} and at most {USERNAME_MAX} characters.\n")
        
        # Checks if username already exist and asks until the given username has not been taken
        usernameInput = user_input.getString("Username: ", USERNAME_MIN, USERNAME_MAX)
        while usernameInput in system.userdb:
            print("Username already exists!\n")
            usernameInput = user_input.getString("Username: ", USERNAME_MIN, USERNAME_MAX)

        # Getting a strong password and name from the user
        passwordInput = user_input.getStrongPassword("Password: ", PASSWORD_MIN, PASSWORD_MAX)
        nameInput = user_input.getString("Name: ")    
        system.userdb[usernameInput] = [nameInput, passwordInput]
        system.user.name = nameInput
        system.user.username = usernameInput

        # Saving user data to database and clearing data from system
        system.userdb.saveData()
        system.userdb.clearData()
        system.changeState(states[2]())