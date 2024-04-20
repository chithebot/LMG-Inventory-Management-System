import time

import create_user
import exit
from ims_constants import *
import ims_tools
import main_menu
import start_menu
import state
import tools
import user_input


class Login(state.State):
    """ This class is the system object's login state which the user
    interacts with to get access to other system features.
    """

    """
    This function handles logging the user into the given system. 

    Args:
        self (Login)    : the current Login object
        system (System) : the System object of interest
    """
    def update(self, system):
        
        # Defining possible states
        states = {1: start_menu.StartMenu, 2: create_user.CreateUser, 3: main_menu.MainMenu, 4: exit.Exit}

        # Read user data into the system user database
        system.userdb.readData()

        # Allows for user to enter username and password a certain number of tries until program terminates
        maxAttempts = 3     # max number of tries to enter username and password
        attempts = 0        # current number of tries
        done = False        # whether or not to continue attempting to log in
        validated = False   # indicates whether or not user has been validated
        headerMsg = None    # header message to be displayed

        while not done and not validated and attempts < maxAttempts:

            # Preparing screen for logging attempt 
            ims_tools.newScreen()
            if headerMsg is not None:
                print(headerMsg, end = "\n")
                headerMsg = None

            # Asking user for username
            print("Enter your username and password.\n")
            usernameInput = user_input.getString("Username: ", 1, USERNAME_MAX)
            
            # Checking that username is valid
            searchResult = system.userdb.get(usernameInput)
            if searchResult is None:
                headerMsg = "Please enter a valid username.\n"
                continue
            
            # Asking user for password associated with user account
            passwordInput = user_input.getString("Password: ", 1, PASSWORD_MAX)
            attempts += 1
            print()

            # Checking if password matches in system database
            validated = (searchResult != None and searchResult[1] == passwordInput)

            # Prompting user if they would like to continue trying to login
            if not validated:
                print(f"Remaining login attempts until lock out: {maxAttempts - attempts}")
                done = (user_input.getYesOrNo("Would you like to continue logging in?") == 'n')
                print()

        # Clearing user data from system memory
        system.userdb.clearData()

        # Handling system state change if not authorized and used all tries
        if not validated and attempts == maxAttempts:
            print("Too many failed login attempts. Exiting system...\n")
            time.sleep(2)
            tools.clearScreen()
            system.changeState(states[4]())

        # Handling system state change if user is authorized
        elif validated:
            system.user.name = searchResult[0]
            system.user.username = usernameInput
            system.changeState(states[3]())

        # Handling system state change if user is not authorized
        else:
            userInput = user_input.getYesOrNo("Would you like to create a new account?")
            if userInput == 'y':
                system.changeState(states[2]())
            else:
                system.changeState(states[1]())