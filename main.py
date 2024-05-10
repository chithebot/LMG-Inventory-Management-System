import inventory_management_system as ims
import unittest
from unit_testall import *

# Program runs here
app = ims.InventoryManagementSystem()
app.run()


def main():

    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()

    #User Section
    suite = loader.loadTestsFromTestCase(TestGetInt)
    suite.addTests(loader.loadTestsFromTestCase(TestGetString))
    suite.addTests(loader.loadTestsFromTestCase(TestContinue))
    suite.addTests(loader.loadTestsFromTestCase(Testyesorno))

    #User Login
    suite.addTests(loader.loadTestsFromTestCase(Testlogin_user))
    suite.addTests(loader.loadTestsFromTestCase(Testlogin_password))
    suite.addTests(loader.loadTestsFromTestCase(Testlogin_password))

    # User Creation
    suite.addTests(loader.loadTestsFromTestCase(TestCreateUser_getUsername))
    suite.addTests(loader.loadTestsFromTestCase(TestCreateUser_getPassword))
    suite.addTests(loader.loadTestsFromTestCase(TestCreateUser_getName))
    suite.addTests(
        loader.loadTestsFromTestCase(TestCreateUser_getSecurityQuestion))
    suite.addTests(
        loader.loadTestsFromTestCase(TestCreateUser_getSecurityQuestionAnswer))
    suite.addTests(loader.loadTestsFromTestCase(TestCreateUser_update))

    # Change Password
    suite.addTests(loader.loadTestsFromTestCase(TestChangePassword_verifyUser))
    suite.addTests(
        loader.loadTestsFromTestCase(TestChangePassword_getPassword))
    suite.addTests(loader.loadTestsFromTestCase(TestChangePassword_update))

    # Logout
    suite.addTests(loader.loadTestsFromTestCase(TestLogout_update))

    # Display Items Menu
    suite.addTests(
        loader.loadTestsFromTestCase(TestDisplayItemsMenu_displayMenu))
    suite.addTests(loader.loadTestsFromTestCase(TestDisplayItemsMenu_update))

    # Display Items All
    suite.addTests(
        loader.loadTestsFromTestCase(TestDisplayItemsAll_displaySortChoices))
    suite.addTests(
        loader.loadTestsFromTestCase(
            TestDisplayItemsAll_displayOrderingChoices))
    suite.addTests(loader.loadTestsFromTestCase(TestDisplayItemsAll_update))

    # Display Categories
    suite.addTests(
        loader.loadTestsFromTestCase(TestDisplayItemsCategory_displayChoices))
    suite.addTests(
        loader.loadTestsFromTestCase(TestDisplayItemsCategory_update))

    #Add/Remove Item Menu
    suite.addTests(
        loader.loadTestsFromTestCase(TestAddRemoveItemMenu_displayMenu))
    suite.addTests(loader.loadTestsFromTestCase(TestAddRemoveItemMenu_update))

    #Add Item
    suite.addTests(loader.loadTestsFromTestCase(TestAddItem_displayInfo))
    suite.addTests(loader.loadTestsFromTestCase(TestAddItem_getItemName))
    suite.addTests(loader.loadTestsFromTestCase(TestAddItem_getItemSKU))
    suite.addTests(loader.loadTestsFromTestCase(TestAddItem_getCategory))
    suite.addTests(loader.loadTestsFromTestCase(TestAddItem_getQuantity))
    suite.addTests(loader.loadTestsFromTestCase(TestAddItem_update))

    #Remove Item
    suite.addTests(loader.loadTestsFromTestCase(TestRemoveItem_update))

    #Add/Remove Category Menu
    suite.addTests(
        loader.loadTestsFromTestCase(TestAddRemoveCategoryMenu_displayMenu))
    suite.addTests(
        loader.loadTestsFromTestCase(TestAddRemoveCategoryMenu_update))

    #Add Category
    suite.addTests(loader.loadTestsFromTestCase(TestAddCategory_update))

    #Remove Category
    suite.addTests(
        loader.loadTestsFromTestCase(TestRemoveCategory_replaceCategoriesAll))
    suite.addTests(loader.loadTestsFromTestCase(TestRemoveCategory_update))

    #Edit Item Menu
    suite.addTests(loader.loadTestsFromTestCase(TestEditMenu_displayMenu))
    suite.addTests(loader.loadTestsFromTestCase(TestEditMenu_update))

    #Edit Item
    suite.addTests(loader.loadTestsFromTestCase(TestEditItem_editName))
    suite.addTests(loader.loadTestsFromTestCase(TestEditItem_editSKU))
    suite.addTests(loader.loadTestsFromTestCase(TestEditItem_editCategory))
    suite.addTests(loader.loadTestsFromTestCase(TestEditItem_editQuantity))
    suite.addTests(
        loader.loadTestsFromTestCase(TestEditItem_getItemIndexToEdit))
    suite.addTests(
        loader.loadTestsFromTestCase(TestEditItem_getAttributesToEdit))
    suite.addTests(loader.loadTestsFromTestCase(TestEditItem_confirmUserEdit))
    suite.addTests(loader.loadTestsFromTestCase(TestEditItem_update))

    # Search Item
    suite.addTests(
        loader.loadTestsFromTestCase(TestSearchItems_displaySearchResults))
    suite.addTests(loader.loadTestsFromTestCase(TestSearchItems_getName))
    suite.addTests(loader.loadTestsFromTestCase(TestSearchItems_getSKU))
    suite.addTests(loader.loadTestsFromTestCase(TestSearchItems_getCategory))
    suite.addTests(loader.loadTestsFromTestCase(TestSearchItems_getQuantity))
    suite.addTests(loader.loadTestsFromTestCase(TestSearchItems_search))
    suite.addTests(loader.loadTestsFromTestCase(TestSearchItems_update))
    result = runner.run(suite)

    return result


if __name__ == "__main__":
    main()
