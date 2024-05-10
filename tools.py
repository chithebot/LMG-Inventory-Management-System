import datetime
import os
import replit


"""
This function opens the given file and displays it on
the console. The ending character of each line can be
defined; the default value is no character.If the file
cannot be opened, an IOError exception is raised.

Args:
    filename (string) : the filename to be displayed
    end (char)        : the ending character of each line

Raises:
    IOError: Raised if file could not be opened
"""
def displayFile(filename, end=''):
    
    with open(filename, mode='r') as file:
        
        # Displaying file
        for line in file:
            print(line, end=end)
        print()


"""
This function gets the number of columns in a file. This
function assumes that all columns, in the file, are equal. 

Args:
    filename (string) : the filename to be displayed

Raises:
    IOError: Raised if file could not be opened

Returns:
    Returns an integer which is the number of columns in
    the file.
"""
def getFileNumCol(filename):

    # Getting the number of columns in the file
    with open(filename, mode='r') as file:
        return len(file.readline())
    

"""
This function clears the terminal screen.
"""
def clearScreen():
    #os.system("cls")     # console/terminal clear screen
    replit.clear()        # replit console clear screen


"""
This function checks if a string contains any characters
in an outlier string. If so, True is returned; False,
otherwise.

Args:
    str (string)     : the string being checked
    outlier (string) : a string containing the excluded characters

Returns:
    Returns True if the checked string contains outlier characters;
    False, otherwise.
"""
def stringContains(str, outlier):

    # Checks if str contains any characters in outlier
    for char in str:
        if char in outlier:
            return True
    return False


"""
This function converts a string to a datetime and returns as
a datetime. If the string cannot be converted, an exception
is raised.

Args:
    str (string) : the string being converted

Returns:
    Returns a datetime object which is the date associated with
    the passed in string
"""
def stringToDatetime(str):
    format = "%Y-%m-%d %H:%M:%S.%f"
    return datetime.datetime.strptime(str, format)