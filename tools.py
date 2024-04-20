import os
import replit


"""
This function opens the given file and displays it on
the console. If the file cannot be opened, an IOError
exception is raised.

Args:
    filename (string) : the filename to be displayed

Raises:
    IOError: Raised if file could not be opened
"""
def displayFile(filename):
    
    with open(filename, mode='r') as file:
        
        # Displaying file
        for line in file:
            print(line, end="")
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
    replit.clear()           # used specifically to clear replit console
    #os.system("cls")        # used for console/terminal based app