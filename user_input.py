import sys


"""
This function gets the user's integer input and returns it. It handles
input checking in the case that an integer is not entered. 

Args:
    prompt (string) : the prompt to display to ask user for input

Returns:
    Returns the user's integer input.
"""
def getInt(prompt):

    # Variable declarations
    valid = False       # tracks validity of the user input
    userInput = 0       # the user's input

    # Gets an integer from the user
    while not valid:

        try:
            userInput = int(input(prompt))
            valid = True
        
        # Handles case where user input is not an integer
        except ValueError:
            print(f"Please enter an integer.\n")

    return userInput


"""
This function gets the user's integer input, within a certain range,
and returns it. It handles input checking in the case that non-integer
characters or integers, not within the specified range, are entered.

    Range: [start, end)

Args:
    prompt (string) : the prompt to display to ask user for input
    start (int)     : the lower bound of the range
    end (int)       : the upper bound of the range which is not included

Raises:
    ValueError : Raised if lower bound is greater than upper bound

Returns:
    Returns the user's integer input.
"""
def getIntRange(prompt, start, end):
    
    # Variable declarations
    valid = False       # tracks validity of the user input
    userInput = 0       # the user's input
    
    # Handles checking that lower bound is not greater than or equal to the upper bound
    if (start >= end):
        raise ValueError("'start' argument cannot be greater than or equal to 'end' argument.")
    
    # Gets an integer from the user
    while not valid:

        try:
            userInput = getInt(prompt)

            # Checking if user input is within the given ranges 
            if (userInput < start) or (userInput >= end):

                # Handles raising exceptions when start and end are not equal and equal
                raise ValueError("Integer must be between " + str(start) + " and " + str(end) +
                                 "; Range = [" + str(start) + ", " + str(end) + ").")
            valid = True            

        except ValueError as e:
            print(e, end="\n\n")

    return userInput


"""
This function gets the user's string input and checks that it is
the appropriate specified length.  

Args:
    prompt (string) : the prompt to display to ask user for input
    min (int)       : the minimum length of the user's input
    max (int)       : the maximum length of the user's input

Raises:
    ValueError : Raised if minimum number of characters is greater than
                 the maximum number of characters 

Returns:
    Returns the user's input.
"""
def getString(prompt, min=0, max=sys.maxsize):
    
    # Variable declarations
    valid = False       # tracks validity of the user input
    userInput = ""      # the user's input

    # Handles checking that min is not greater than max
    if (min > max):
        raise ValueError("'min' argument cannot be greater than 'max' argument.")

    # Gets a string input from the user 
    while not valid:

        try:
            userInput = input(prompt) 

            # Checking if user input the appropriate length 
            if len(userInput) < min:
                raise ValueError("Input must contain at least " + str(min) + " characters.")
            if len(userInput) > max:
                raise ValueError("Input must contain at most " + str(max) + " characters.")
            valid = True            

        except ValueError as e:
            print(e, end="\n\n")
    return userInput.strip()


"""
This function gets a strong password from the user.  

Args:
    prompt (string) : the prompt to display to ask user for input
    min (int)       : the minimum length of the user's input
    max (int)       : the maximum length of the user's input

Raises:
    ValueError : Raised if minimum number of characters is greater than
                 the maximum number of characters 

Returns:
    Returns the user's input.
"""
def getStrongPassword(prompt, min=12, max=sys.maxsize):
    
    # Variable declarations
    valid = False       # tracks validity of the user input
    userInput = ""      # the user's input

    # Gets a string input from the user 
    while not valid:

        try:
            userInput = getString(prompt, min, max)

            # Strong password checklist
            uppercase = False       # Tracks if user input has an uppercase
            lowercase = False       # Tracks if user input has a lowercase
            symbol = False          # Tracks if user input has a symbol
            number = False          # Tracks if user input has a number

            # Checking if user input contains characteristics of strong password 
            for char in userInput:

                # Checking if character meets any strong password criteria
                if char.isupper():
                    uppercase = True
                elif char.islower():
                    lowercase = True
                elif char.isnumeric():
                    number = True
                elif char in "~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/!@":
                    symbol = True

            # Throwing exceptions if password does not meet criteria
            if not (uppercase and lowercase and number and symbol):
                
                # Building error string
                errorString = "The password "
                if not uppercase:
                    errorString += "must contain at least one uppercase; "
                if not lowercase:
                    errorString += "must contain at least one lowercase; "
                if not symbol:
                    errorString += "must contain at least one symbol; "
                if not number:
                    errorString += "must contain at least one number; "

                # Formatting error string ending
                errorString = errorString[:len(errorString) - 2] + '.'
                raise ValueError(errorString)
            
            valid = True

        except ValueError as e:
            print(e, end="\n\n")
    return userInput


"""
This function pauses the program until the user presses any key
to continue.  

Args:
    prompt (string) : the prompt to display to ask user for input
"""
def getContinue(prompt="Press any key to continue.\n"):

    input(prompt)


"""
This function gets the user's input of yes (y) or no (n) and returns
it. The function handles prompting the user until an appropriate
input has been entered.

Args:
    prompt (string) : the prompt to display to ask user for input

Returns:
    Returns the lowercase form of the user's input.
"""
def getYesOrNo(prompt):
    
    # Variable declarations
    valid = False       # tracks validity of the user input
    userInput = ""      # the user's input

    # Gets a string input from the user 
    while not valid:

        try:
            userInput = input(prompt + " [Y/n] ") 

            # Checking if user input is valid
            if len(userInput) != 1:
                raise ValueError("Invalid input! Input size must be 1 character.") 
            elif userInput.lower() not in "yn":
                raise ValueError("Invalid input! Valid inputs are: [Y, N, y, n]")
            valid = True            

        except ValueError as e:
            print(e, end="\n\n")
    return userInput.lower()