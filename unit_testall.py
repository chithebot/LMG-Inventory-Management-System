from add_category import AddCategory
import add_remove_item_menu as arim
from change_password import ChangePassword
from create_user import CreateUser
from display_items_all import DisplayItemsAll
from display_items_category import DisplayItemsCategory
import display_items_menu as dim
from edit_item import EditItem
import edit_item_menu as eim
import ims_tools
import logout
import menu
from remove_category import RemoveCategory
from remove_item import RemoveItem
import search_items as si
import state
import user_input
import unittest
from unittest.mock import patch, MagicMock
import sys
import unittest
import user_input
from unittest.mock import patch
from unittest import TestCase, main
import system as sys1
from add_item import AddItem
from add_remove_category_menu import AddRemoveCategoryMenu
import ims_tools


# Some classes are abstract classes,unused or perform similar so they have no uni
#user section
class TestGetInt(TestCase):

    @patch('builtins.input', side_effect=['10'])
    def test_get_int_positive(self, mock_input):
        # Test cases for positive integers
        prompt_message = "Enter a positive integer: "
        result = user_input.getInt(prompt_message)
        self.assertEqual(result, 10)


class TestGetString(TestCase):

    @patch('builtins.input', side_effect=['10'])
    def test_get_int_positive(self, mock_input):
        # Test cases for positive integers
        prompt_message = "Test"
        result = user_input.getString("Test")
        self.assertEqual(result, '10')


class TestContinue(TestCase):

    @patch('builtins.input', side_effect=['y'])
    def test_continue(self, mock_input):
        result = user_input.getString("Test")
        self.assertEqual(result, 'y')


class Testyesorno(TestCase):

    @patch('builtins.input', side_effect=['y'])
    def test_yesorno(self, mock_input):
        result = user_input.getString("Test")
        self.assertEqual(result, 'y')


# Login Section
class Testlogin_user(TestCase):

    @patch('builtins.input', side_effect=['Victor'])
    def test_validateUsername(self, mock_input):
        result = user_input.getString('Victor')
        self.assertEqual(result, 'Victor')


class Testlogin_password(TestCase):

    @patch('builtins.input', side_effect=['PCC_WARRIOR'])
    def test_validateUsername(self, mock_input):
        result = user_input.getString('PCC_WARRIOR')
        self.assertEqual(result, 'PCC_WARRIOR')


# User Creation
class TestCreateUser_getUsername(TestCase):

    def test_getUsername(self):
        self.assertTrue(hasattr(CreateUser, 'getUsername'), "fail")


class TestCreateUser_getPassword(TestCase):

    def test_getPassword(self):
        self.assertTrue(hasattr(CreateUser, 'getPassword'), "fail")


class TestCreateUser_getName(TestCase):

    def test_getName(self):
        self.assertTrue(hasattr(CreateUser, 'getName'), "fail")


class TestCreateUser_getSecurityQuestion(TestCase):

    def test_getSecurityQuestion(self):
        self.assertTrue(hasattr(CreateUser, 'getSecurityQuestion'), "fail")


class TestCreateUser_getSecurityQuestionAnswer(TestCase):

    def test_getSecurityQuestionAnswer(self):
        self.assertTrue(hasattr(CreateUser, 'getSecurityQuestionAnswer'),
                        "fail")


class TestCreateUser_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(CreateUser, 'update'), "fail")


# Change Password
class TestChangePassword_verifyUser(TestCase):

    def test_verifyUser(self):
        self.assertTrue(hasattr(ChangePassword, 'verifyUser'), "fail")


class TestChangePassword_getPassword(TestCase):

    def test_getPassword(self):
        self.assertTrue(hasattr(ChangePassword, 'getPassword'), "fail")


class TestChangePassword_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(ChangePassword, 'update'), "fail")


# Logout
class TestLogout_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(logout.Logout, 'update'), "fail")


#Display Items Menu
class TestDisplayItemsMenu_displayMenu(TestCase):

    def test_displayMenu(self):
        self.assertTrue(hasattr(dim.DisplayItemsMenu, 'displayMenu'), "fail")


class TestDisplayItemsMenu_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(dim.DisplayItemsMenu, 'update'), "fail")


#Display Items All
class TestDisplayItemsAll_displaySortChoices(TestCase):

    def test_displaySortChoices(self):
        self.assertTrue(hasattr(DisplayItemsAll, 'displaySortChoices'), "fail")


class TestDisplayItemsAll_displayOrderingChoices(TestCase):

    def test_displayOrderingChoices(self):
        self.assertTrue(hasattr(DisplayItemsAll, 'displayOrderingChoices'),
                        "fail")


class TestDisplayItemsAll_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(DisplayItemsAll, 'update'), "fail")


#Display Categories
class TestDisplayItemsCategory_displayChoices(TestCase):

    def test_displayChoices(self):
        self.assertTrue(hasattr(DisplayItemsCategory, 'displayChoices'),
                        "fail")


class TestDisplayItemsCategory_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(DisplayItemsCategory, 'update'), "fail")


#Add/Remove Items section
class TestAddRemoveItemMenu_displayMenu(TestCase):

    def test_displayMenu(self):
        self.assertTrue(hasattr(arim.AddRemoveItemMenu, 'displayMenu'), "fail")


class TestAddRemoveItemMenu_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(arim.AddRemoveItemMenu, 'update'), "fail")


class TestAddItem_displayInfo(unittest.TestCase):

    @patch('add_item.ims_tools.newScreen')
    @patch('add_item.ims_tools.displayItemInfo')
    def test_displayInfo_calls_ims_tools_functions(self, mock_displayItemInfo,
                                                   mock_newScreen):
        system = MagicMock(
        )  # You'll need to create a mock object for the system argument
        header = "Test"

        # Call the method under test
        AddItem().displayInfo(system, header, "Xbox")

        # Check if the functions were called once
        mock_newScreen.assert_called_once()
        mock_displayItemInfo.assert_called_once()


class TestAddItem_getItemName(TestCase):

    @patch('add_item.user_input.getString')
    def test_getItemName(self, mock_getString):
        mock_system = MagicMock()
        mock_getString.return_value = "Test Item"  # Mock the user input

        # Call the method under test
        AddItem().getItemName(mock_system)
        mock_getString.assert_called_once()


class TestAddItem_getItemSKU(unittest.TestCase):

    @patch('add_item.user_input.getIntRange')
    def test_getItemSKU(self, mock_getIntRange):
        mock_system = MagicMock()  # Mock the system object

        # Call the method under test
        AddItem().getItemSKU(mock_system)

        # Check if getIntRange was called
        mock_getIntRange.assert_called_once()


class TestAddItem_getCategory(TestCase):

    def test_getCategory(self):
        self.assertTrue(hasattr(AddItem, 'getCategory'), "fail")


class TestAddItem_getQuantity(TestCase):

    def test_getCategory(self):
        self.assertTrue(hasattr(AddItem, 'getQuantity'), "fail")


class TestAddItem_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(AddItem, "update"), "fail")


class TestRemoveItem_update(TestCase):

    def test_(self):
        self.assertTrue(hasattr(RemoveItem, 'update'), "fail")


# Edit Item
class TestEditMenu_displayMenu(TestCase):

    def test_displayMenu(self):
        self.assertTrue(hasattr(eim.EditItemMenu, 'displayMenu'), "fail")


class TestEditMenu_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(eim.EditItemMenu, 'update'), "fail")


class TestEditItem_editName(TestCase):

    def test_editName(self):
        self.assertTrue(hasattr(EditItem, 'editName'), "fail")


class TestEditItem_editSKU(TestCase):

    def test_editSKU(self):
        self.assertTrue(hasattr(EditItem, 'editSKU'), "fail")


class TestEditItem_editCategory(TestCase):

    def test_editCategory(self):
        self.assertTrue(hasattr(EditItem, 'editCategory'), "fail")


class TestEditItem_editQuantity(TestCase):

    def test_editQuantity(self):
        self.assertTrue(hasattr(EditItem, 'editQuantity'), "fail")


class TestEditItem_getItemIndexToEdit(TestCase):

    def test_getItemIndexToEdit(self):
        self.assertTrue(hasattr(EditItem, 'getItemIndexToEdit'), "fail")


class TestEditItem_getAttributesToEdit(TestCase):

    def test_getAttributesToEdit(self):
        self.assertTrue(hasattr(EditItem, 'getAttributesToEdit'), "fail")


class TestEditItem_confirmUserEdit(TestCase):

    def test_confirmUserEdit(self):
        self.assertTrue(hasattr(EditItem, 'confirmUserEdit'), "fail")


class TestEditItem_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(EditItem, 'update'), "fail")


# Search Items Section
class TestSearchItems_displaySearchResults(TestCase):

    def test_displaySearchResults(self):
        self.assertTrue(hasattr(si.SearchItems, 'displaySearchResults'),
                        "fail")


class TestSearchItems_getName(TestCase):

    def test_getName(self):
        self.assertTrue(hasattr(si.SearchItems, 'getName'), "fail")


class TestSearchItems_getSKU(TestCase):

    def test_getSKU(self):
        self.assertTrue(hasattr(si.SearchItems, 'getSKU'), "fail")


class TestSearchItems_getCategory(TestCase):

    def test_getCategory(self):
        self.assertTrue(hasattr(si.SearchItems, 'getCategory'), "fail")


class TestSearchItems_getQuantity(TestCase):

    def test_getQuantity(self):
        self.assertTrue(hasattr(si.SearchItems, 'getQuantity'), "fail")


class TestSearchItems_search(TestCase):

    def test_search(self):
        self.assertTrue(hasattr(si.SearchItems, 'search'), "fail")


class TestSearchItems_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(si.SearchItems, 'update'), "fail")


#Category section
class TestAddRemoveCategoryMenu_displayMenu(TestCase):

    def test_displayMenu(self):
        self.assertTrue(hasattr(AddRemoveCategoryMenu, 'displayMenu'), "fail")


class TestAddRemoveCategoryMenu_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(AddRemoveCategoryMenu, 'update'), "fail")


class TestAddCategory_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(AddCategory, 'update'), "fail")


class TestRemoveCategory_replaceCategoriesAll(TestCase):

    def test_replaceCategoriesAll(self):
        self.assertTrue(hasattr(RemoveCategory, 'replaceCategoriesAll'),
                        "fail")


class TestRemoveCategory_update(TestCase):

    def test_update(self):
        self.assertTrue(hasattr(RemoveCategory, 'update'), "fail")


#class Test(TestCase):
#    def test_(self):
#        self.assertTrue(hasattr(<class_name>, 'func_name'), "fail")

if __name__ == '__main__':
    unittest.main()
#database section
