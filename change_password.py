from ims_constants import *
import ims_tools
import start_menu
import state
import user_input


class ChangePassword(state.State):
    """ This class is the system object's change password state which
    the user interacts with to change their password.
    """

    """
    This function handles checking that the user is verified by asking
    them the account security question. True is returned if the account
    is not verified; False, otherwise.

    Args:
        self (ChangePassword) : the current ChangePassword object
        user (User)           : the User object containing the account
                                the current user is trying to access
    
    Returns:
        Returns True if the user is verified to be an authorized
        user; False, otherwise.
    """
    def verifyUser(self, user):

        # Getting security question and security question answer associated with account
        sqFilename = "assets/security_questions.txt"
        with open(sqFilename) as file:

            for i in range(user.security_question):
                file.readline()
            securityQuestion = file.readline()[:-1]

        # Displaying security question
        ims_tools.newScreen()
        print("Answer the following security question to change your password.")
        print(securityQuestion)

        # Getting user input for their security answer
        userInput = user_input.getString("Answer: ", 1)
        return userInput == user.security_question_ans


    """
    This function handles getting user input on the new password they
    wish to change to and returns it.

    Args:
        self (ChangePassword) : the current ChangePassword object
    
    Returns:
        Returns the password received from the user.
    """
    def getPassword(self):

        password = ""
        passwordConfirm = ""
        done = False        # checks if new password is same after user inputs their new password
        error = False
        errorMsg = "Password you retyped is not the same as the password you entered in the first password field."
        
        # Getting new password from user and handles password reconfirmation
        while not done:

            # Preparing screen and displaying error message if there are any
            ims_tools.newScreen()
            if error:
                print(errorMsg + '\n')
                error = False

            # Getting new password from user
            print("Enter your new password.")
            password = user_input.getStrongPassword("Password: ", PASSWORD_MIN, PASSWORD_MAX, outliers=" ")
            passwordConfirm = user_input.getStrongPassword("Retype Password: ", PASSWORD_MIN, PASSWORD_MAX, outliers=" ")
            done = (password == passwordConfirm)
            
            # Setting error flag if password and retyped password are not same
            if not done:
                error = True
        return password


    """
    This function handles getting user input on the username that is associated
    with the account they desire to change the password of. It validating that
    the user is an authorized user by having them answer their security question
    which then allows them to change the password if they answered correctly.

    Args:
        self (ChangePassword) : the current ChangePassword object
        system (System)       : the System object of interest
    """
    def update(self, system):

        # Loads user data into the system if not already loaded
        if not system.userLoaded:
            system.userdb.readData()
            system.userLoaded = True

        # Changing password loop
        done = False
        changed = False
        while not done:
            
            # Preparing new screen
            ims_tools.newScreen()
            print("Please enter the username you wish to change the password of.")

            # Getting user input on username of account
            username = user_input.getString("Enter the username: ", 1, USERNAME_MAX)
            usr = system.userdb.get(username)

            # Verifying that account, associated with username, exists in user database
            if usr is not None:

                # Verifying that current user is an authorized user of account
                verified = self.verifyUser(usr)

                # Changing password of user and unlocking account
                if verified:
                    password = self.getPassword()
                    usr.password = password
                    usr.unlock()
                    system.userdb.saveData()
                    done = True
                    changed = True
            
            # Asking user if they would like to try to put another account
            if not changed:
                done = (user_input.getYesOrNo("Would you like to try again?") == 'n')

        # Moving system state to start menu
        system.changeState(start_menu.StartMenu())