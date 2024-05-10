# User and Item class CONSTANTS
# Max character length of Item attributes
NAME_MAX = 32
SKU_MAX = 6
CATEGORY_MAX = 18
QUANTITY_MAX = 10

# Max and Min SKU value
SKU_MAX_VALUE = 999999
SKU_MIN_VALUE = 100000

# Max and Min Quantity value
QUANTITY_MAX_VALUE = 1000000
QUANTITY_MIN_VALUE = 0

# Login/CreateUser CONSTANTS
# character length boundaries on username and password
USERNAME_MIN = 6
USERNAME_MAX = 32
PASSWORD_MIN = 8
PASSWORD_MAX = 32
MAX_LOGIN_ATTEMPTS = 3
MINS_PASS_UNLOCK = 30
NUM_SECURITY_QUESTIONS = 9
SECURITY_QUESTION_ANS_MIN = 1
SECURITY_QUESTION_ANS_MAX = 64

# DisplayAllItems CONSTANTS
# user input choices on sorting method
SORT_NAME = 1
SORT_SKU = 2
SORT_CATEGORY = 3
SORT_QUANTITY = 4
QUIT_DISPLAY_ALL = 5    # quit display input

# user input choices on sorting order
ASCENDING = 1
DESCENDING = 2

# SearchItems and EditItem CONSTANTS
# user input choice for not search or edit by certain attribute
NO_SEARCH = -1
NO_SEARCH_STR = "-1"
NO_EDIT = -1
NO_EDIT_STR = "-1"