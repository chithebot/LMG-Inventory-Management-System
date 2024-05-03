import datetime

from ims_constants import *
import ims_tools
import main_menu
import start_menu
import state
import user_input


class Login(state.State):
    """ This class is the system object's login state which the user
    interacts with to get access to other system features.
    """


    """
    This function handles validating the passed in username with the system
    user database. If the username is validated, True is returned; False,
    otherwise. On the failure to validate the username, messsages are printed
    onto the console to indicate what was the cause of failure.

    Args:
        self (Login)      : the current Login object
        system (System)   : the System object of interest
        username (string) : the username of the object

    Returns:
        Returns True if the username is validated; False, otherwise.
    """
    def validateUsername(self, system, username):
        
        # Validating that username exists in system user database
        usr = system.userdb.get(username)
        failureMsg = ""
        if usr is not None:

            # Unlocking account if it is possible
            if usr.isUnlockable():
                usr.unlock()

            # Handles cases if the account is not locked
            if not usr.isLocked():
                return True, failureMsg
            
            # Handles case for account being locked
            failureMsg = "The account you are trying to access is locked.\n"
            failureMsg += f"You are locked out for {usr.getRemainingLockDuration():.1f} more minutes.\n"
            failureMsg += "Please reset the password in the start menu to unlock it.\n"

        else:
            failureMsg = "The account you are trying to access does not exist.\n"
        return False, failureMsg


    """
    This function handles validating the passed in password with the passed
    in username in the system user database. If the username is validated, 
    True is returned; False, otherwise. On the failure to validate the
    username, messsages are printed onto the console to indicate what was
    the cause of failure.

    Args:
        self (Login)      : the current Login object
        system (System)   : the System object of interest
        username (string) : the username of the user
        password (string) : the password of the user

    Returns:
        Returns True if the password is validated; False, otherwise.
    """
    def validatePassword(self, system, username, password):
        
        # Validating that password
        failureMsg = ""
        usr = system.userdb.get(username)
        if usr is not None and usr.password == password:
            return True, failureMsg
        
        # Handles validation failure
        usr.last_login_attempt = datetime.datetime.now()
        usr.login_attempts += 1
        failureMsg = f"You have {MAX_LOGIN_ATTEMPTS - usr.login_attempts} login attempts left before this account is locked.\n"
        return False, failureMsg


    """
    This function handles logging the user into the given system. 

    Args:
        self (Login)    : the current Login object
        system (System) : the System object of interest
    """
    def update(self, system):
        
        # Defining possible states
        states = {1: start_menu.StartMenu, 2: main_menu.MainMenu}

        # Loads user data into the system if not already loaded
        if not system.userLoaded:
            system.userdb.readData()
            system.userLoaded = True

        # Allows for user to enter username and password a certain number of tries until program terminates
        done = False        # whether or not to continue attempting to log in
        validated = False   # indicates whether or not user has been validated

        while not done and not validated:

            # Preparing screen for logging attempt 
            ims_tools.newScreen()

            # Asking user for username and password
            print("Enter your username and password.\n")
            usernameInput = user_input.getString("Username: ", 1, USERNAME_MAX)
            passwordInput = user_input.getString("Password: ", 1, PASSWORD_MAX)
            print()

            # Validation phase
            usernameValidated, failureMsg = self.validateUsername(system, usernameInput)
            passwordValidated = False

            # Validating password
            if usernameValidated:
                passwordValidated, failureMsg = self.validatePassword(system, usernameInput, passwordInput)

            # Prompting user if they would like to continue trying to login
            validated = usernameValidated and passwordValidated
            if not validated:
                print(failureMsg)
                done = (user_input.getYesOrNo("Would you like to continue logging in?") == 'n')
                print()

        # Handles case where user is validated and can log in
        if validated:
            usr = system.userdb[usernameInput]
            usr.unlock()                            # resets login attempts
            system.user.name = usr.name
            system.user.username = usr.username
            system.changeState(states[2]())
        else:
            system.changeState(states[1]())
        system.userdb.saveData()