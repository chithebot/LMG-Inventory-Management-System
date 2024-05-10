import ims_tools
from ims_constants import *
import main_menu
import start_menu
import state
import user
import user_input


class CreateUser(state.State):
    """ This class is the system object's create user state which a
    user interacts with to create an account to access more system
    features.
    """


    """
    This function handles getting the username from the user. It
    handles checking for any existing username.

    Args:
        self (CreateUser) : the current CreateUser object
        system (System)   : the System object of interest
    
    Returns:
        Returns the user's input for the username.
    """
    def getUsername(self, system):

        # Welcoming user and displaying username restrictions
        print("Welcome new user! Enter your desired username to get started!")
        print(f"The username must have at least {USERNAME_MIN} and at most {USERNAME_MAX} characters.\n")
        
        # Checks if username already exist and asks until the given username has not been taken
        usernameInput = user_input.getString("Username: ", USERNAME_MIN, USERNAME_MAX, outliers=" ")

        while usernameInput in system.userdb:
            print("Username already exists!\n")
            usernameInput = user_input.getString("Username: ", USERNAME_MIN, USERNAME_MAX, outliers=" ")
        return usernameInput

    """
    This function handles getting the password from the user.

    Args:
        self (CreateUser) : the current CreateUser object
        system (System)   : the System object of interest
    
    Returns:
        Returns the user's input for the password.
    """
    def getPassword(self, system):
        return user_input.getStrongPassword("Password: ", PASSWORD_MIN, PASSWORD_MAX, outliers=" ")


    """
    This function handles getting the name from the user.

    Args:
        self (CreateUser) : the current CreateUser object
        system (System)   : the System object of interest
    
    Returns:
        Returns the user's input for the name.
    """
    def getName(self, system):
        return user_input.getString("Enter your name: ", 1, NAME_MAX)


    """
    This function handles getting the security question from the
    user.

    Args:
        self (CreateUser) : the current CreateUser object
        system (System)   : the System object of interest
    
    Returns:
        Returns the user's input for the security question.
    """
    def getSecurityQuestion(self, system):
        ims_tools.displaySecurityQuestions()
        print()
        return user_input.getIntRange("Enter the security question to use when recovering your account: ",
                                      1, NUM_SECURITY_QUESTIONS + 1)


    """
    This function handles getting the security question answer
    from the user.

    Args:
        self (CreateUser) : the current CreateUser object
        system (System)   : the System object of interest
    
    Returns:
        Returns the user's input for the security question
        answer.
    """
    def getSecurityQuestionAnswer(self, system):
        return user_input.getString("Enter your answer to the security question: \n",
                                    SECURITY_QUESTION_ANS_MIN, SECURITY_QUESTION_ANS_MAX)


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

        # Loads user data into the system if not already loaded
        if not system.userLoaded:
            system.userdb.readData()
            system.userLoaded = True

        # Getting new user information from user
        done = False            # tracks if the user wants to quit account creation
        created = False         # tracks if an account was created
        while not done and not created:

            # Defining function and attribute dictionary
            funcList = [self.getName,self.getUsername, self.getPassword, self.getSecurityQuestion, self.getSecurityQuestionAnswer]
            attrList = ["name","username", "password", "security_question", "security_question_ans"]

            # Getting User information
            newUser = user.User()
            #displayUserInfo = info.info
            for i in range(len(funcList)):
                ims_tools.newScreen()
                ims_tools.displayUserInfo("New User Information", newUser)
                setattr(newUser, attrList[i], funcList[i](system))
            # Confirming user information
            ims_tools.newScreen()
            ims_tools.displayUserInfo("New User Information", newUser)
            done = (user_input.getString("Is this information correct? (y/n): ") ==['y', 'n'])
            if done:
                created = system.userdb.createUser(newUser)
                if created:
                    print("Account created! Please log in to continue.")
                  
            # Saving new user data to database and changing system state
            confirm = (user_input.getYesOrNo("Please confirm the creation of this account.") == 'y')
            if confirm:
                system.user.name = newUser.name             # setting current System user to the new User
                system.userdb[newUser.username] = newUser   # adding new User to database
                system.userdb.saveData()                    # saving new User to database
                system.user.username = newUser.username
                created = True
            
            # Handles asking user if they want to try creating an account again
            else:
                done = (user_input.getYesOrNo("Would you like to try making an account again?") == 'n')

        # Moving system to appropriate state depending on if account was created
        if not created:
            system.changeState(states[1]())
        else:
            system.changeState(states[2]())