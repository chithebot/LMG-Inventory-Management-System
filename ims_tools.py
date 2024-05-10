from ims_constants import *
import tools


"""
This function displays the IMS title. 

Raises:
    IOError: Raised if file could not be opened
"""
def displayTitle():

    # Displaying the title
    titleFile = "assets/title.txt"
    tools.displayFile(titleFile)


"""
This function displays the developer group's name. 

Raises:
    IOError: Raised if file could not be opened
"""
def displayDevGroup():

    # Displaying the developer group name
    devNameFile = "assets/dev_name.txt"
    tools.displayFile(devNameFile)


"""
This function displays the IMS application header. 

Raises:
    IOError: Raised if file could not be opened
"""
def displayIMSHeader():

    # Displaying the application header
    appHeaderFile = "assets/app_header.txt"
    tools.displayFile(appHeaderFile)
    print(tools.getFileNumCol(appHeaderFile) * '-')


"""
This function clears the screen and displays the
IMS application header. 

Raises:
    IOError: Raised if file could not be opened
"""
def newScreen():
    tools.clearScreen()
    displayIMSHeader()
    print()


"""
This function displays all item information in the passed
in list of items. The starting entry number can be defined
by the user; the default starting value is 1. Starting entry
must be a non-negative integer.

Args:
    items (list<Item>) : a list of Item objects
    entryStart (int)   : the starting entry to begin with

Raises:
    ValueError : Raised when starting entry is negative.
"""
def displayItems(items, entryStart=1):

    # Checks that starting entry is non-negative
    if entryStart < 0:
        raise ValueError("Starting entry must be non-negative.")

    # Spacings in each column
    numDigitEntries = len(str(len(items)))
    entryNumSpacing = max(numDigitEntries, len("Entry")) + 2
    nameSpacing = NAME_MAX + 2
    skuSpacing = SKU_MAX + 2
    categorySpacing = CATEGORY_MAX + 2
    quantitySpacing = QUANTITY_MAX + 2

    # Displaying item header
    itemHeader = f"|{'Entry'.center(entryNumSpacing)}|{'Name'.center(nameSpacing)}|{'SKU'.center(skuSpacing)}|"
    itemHeader += f"{'Category'.center(categorySpacing)}|{'Quantity'.center(quantitySpacing)}|"
    print('-' * len(itemHeader))
    print(itemHeader)
        
    # Displaying all items in the items database
    entry = entryStart          # the item entry in data
    leftPadding = 1             # padding on left side of table
    for item in items:
        itemInfo = f"|{str(entry).center(entryNumSpacing)}|{(leftPadding * ' ' + item.name).ljust(nameSpacing)}|"
        itemInfo += f"{str(item.sku).center(skuSpacing)}|{(item.category).center(categorySpacing)}|{str(item.quantity).center(quantitySpacing)}|"
        entry += 1
        print('-' * len(itemInfo))
        print(itemInfo) 
    print('-' * len(itemHeader) + '\n')


"""
This function displays all categories from the passed
in list of categories. The starting entry number can be
defined by the user; the default starting value is 1.
Starting entry must be a non-negative integer.

Args:
    items (list<Category>) : a list of Category objects
    entryStart (int)       : the starting entry to begin with

Raises:
    ValueError : Raised when starting entry is negative.
"""
def displayCategories(categories, entryStart=1):

    # Checks that starting entry is non-negative
    if entryStart < 0:
        raise ValueError("Starting entry must be non-negative.")

    # Defining column spacings
    numDigitEntries = len(str(len(categories)))
    entryNumSpacing = max(numDigitEntries, len("Entry")) + 2
    categorySpacing = CATEGORY_MAX + 2

    # Displaying category header
    categoryHeader = f"|{'Entry'.center(entryNumSpacing)}|{'Category'.center(categorySpacing)}|"
    print('-' * len(categoryHeader))
    print(categoryHeader)
        
    # Displaying all items in the items database
    entry = entryStart
    for category in categories:
        categoryInfo = f"|{str(entry).center(entryNumSpacing)}|{category.center(categorySpacing)}|"
        print('-' * len(categoryInfo))
        print(categoryInfo)
        entry += 1
    print('-' * len(categoryHeader) + '\n')


"""
This function displays an item's information onto the console/terminal. 

Args:
    header (string) : the header for the item being displayed
    item (Item)     : the Item object of to be displayed
"""
def displayItemInfo(header, item):

    # Displaying new item
    print(header)
    print(f"Name: {item.name}\n" +
          f"SKU: {item.sku}\n" + 
          f"Category: {item.category}\n" +
          f"Quantity: {item.quantity}\n")



"""
This function displays the security questions onto the console.

Raises:
    IOError : Raised when file failed to open.
"""
def displaySecurityQuestions():
    
    # Opening file containing security questions
    filename = "assets/security_questions.txt"
    with open(filename) as file:

        # Displaying security questions
        entry = 1
        for line in file:
            print(f"{entry}. " + line, end="")
            entry += 1



"""
This function displays a user's information onto the console/terminal. 

Args:
    header (string) : the header for the item being displayed
    user (User)     : the Item object of to be displayed
"""
def displayUserInfo(header, user):

    # Getting security question
    security_question = "None"
    if user.security_question is not None:

        filename_sq = "assets/security_questions.txt"
        with open(filename_sq) as file:
            for i in range(user.security_question):
                security_question = file.readline()[:-1]

    # Getting security question answer in string form
    security_question_ans = "None"
    if user.security_question_ans is not None:
        security_question_ans = user.security_question_ans

    # Displaying user information
    print(header)
    print(f"Name: {user.name}\n" +
          f"Username: {user.username}\n" +
          f"Password: {user.password}\n" +
          f"Security Question: {security_question}\n" +
          f"Security Question Answer: {security_question_ans}\n")


"""
This function checks if a given item name already exists in
the passed in list of items. If the item name exists in the
item list then True is returned; False, otherwise.

Args:
    itemName (string)     : the item name to search for
    itemList (list<Item>) : the list containing Item objects

Returns:
    Returns True if the item name already exists in the item
    list; False, otherwise.
"""
def nameExistIn(itemName, itemList):

    # Checking if name already exists in the item list
    for item in itemList:
        if item.name == itemName:
            return True
    return False


"""
This function checks if a given item SKU already exists in
the passed in list of items. If the item SKU exists in the
item list then True is returned; False, otherwise.

Args:
    itemSKU (int)         : the item SKU to search for
    itemList (list<Item>) : the list containing Item objects

Returns:
    Returns True if the item SKU already exists in the item
    list; False, otherwise.
"""
def SKUExistIn(itemSKU, itemList):

    # Checking if SKU already exists in the item list
    for item in itemList:
        if item.sku == itemSKU:
            return True
    return False