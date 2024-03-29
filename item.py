import entity


class Item(entity.Entity):
    """ This class represents an item in a warehouse.

        Attributes:
            _sku (int)          : the item's identifier number
            _category (string)  : the item's category
            _quantity (int)     : the item's quantity
    """
    __doc__ += ('\n' + entity.Entity.__doc__)

    """
    This function initializes an Item object.

    Args:
        self (Item)		    : the current Item object
        name (string)	    : the name of the Item object
        sku (int)	        : the ID of the Item object
        category (string)	: the category the Item object belongs to
        quantity (int)	    : the quantity of the Item object
    """ 
    def __init__(self, name="", sku=0, category="", quantity=0):
        super().__init__(name)
        self._sku = sku
        self._category = category
        self._quantity = quantity


    """
    This function gets the current Item object's SKU.

    Args:
        self (Item) : the current Item object
        sku (int)   : the ID of the Item object

    Returns:
        Returns the Item object's SKU.
    """
    @property
    def sku(self):
        return self._sku


    """
    This function gets the current Item object's category.

    Args:
        self (Item)		    : the current Item object
        category (string)	: the category the Item object belongs to

    Returns:
        Returns the Item object's category.
    """
    @property
    def category(self):
        return self._category


    """
    This function gets the current Item object's quantity.

    Args:
        self (Item)     : the current Item object
        quantity (int)  : the quantity of the Item object

    Returns:
        Returns the Item object's quantity.
    """
    @property
    def quantity(self):
        return self._quantity


    """
    This function gets the string representation of the current Item object.

    Args:
        self (Item) : the current Item object

    Returns:
        Returns the string representation of the current Item object.
    """
    def __str__(self):
        itemInfo = super().__str__() + " (" + str(self.sku) + ") : " + \
                   self.category + " : " + str(self.quantity) + " units"
        return itemInfo


    """
    This function checks if the current Item object, and passed in Item
    object, are equal. Their equivalency is determined whether or not their
    name and SKU are equal.

    Args:
        self (Item)     : the current Item object being compared
        other (Item)	: the other Item object being compared

    Returns:
        Returns true if the Item objects are equal; false, otherwise.
    """
    def __eq__(self, other):
        return self.sku == other.sku and self.name == other.name


    """
    This function checks if the current Item object is less than the 
    passed in Item object. Their SKU is used to determine whether or
    not an Item object precedes another. This is mostly used for
    sorting purposes.

    Args:
        self (Item)		: the current Item object being compared
        other (Item)	: the other Item object being compared

    Returns:
        Returns true if the current Item object is less than the
        passed in Item object; false, otherwise.
    """
    def __lt__(self, other):
        return self.sku < other.sku


    """
    This function sets the current Item's SKU.

    Args:
        self (Item) : the current Item object
        sku (int)   : the new SKU to be set
    """
    @sku.setter
    def sku(self, sku):
        self._sku = sku


    """
    This function sets the current Item's category.

    Args:
        self (Item)		    : the current Item object
        category (string)	: the new category to be set
    """
    @category.setter
    def category(self, category):
        self._category = category


    """
    This function sets the current Item's quantity.

    Args:
        self (Item)     : the current Item object
        quantity (int)  : the new quantity to be set
    """
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity


    """
    This function adds the given integer value to the current Item object.
    To guard against undefined behavior, quantity values must be non-negative.
    
    Args:
        self (Item)		: the current Item object being compared
        quantity (int)	: the quantity to add

    Returns:
        Returns the current Item object.
    
    Raises:
        ValueError: Raised if quantity is negative.
    """
    def __iadd__(self, quantity):

        # Handles case of negative quantity values
        if (quantity < 0):
            raise ValueError("Quantity must be a non-negative integer value.")
        self.quantity += quantity
        return self


    """
    This function subtracts the given integer value to the current Item object.
    To guard against undefined behavior, quantity values must be non-negative.

    Args:
        self (Item)		: the current Item object being compared
        quantity (int)	: the quantity to subtract

    Returns:
        Returns the current Item object.

    Raises:
        ValueError: Raised if quantity is negative.
        ValueError: Raised if quantity exceeds quantity of current Item object.
    """
    def __isub__(self, quantity):

        # Handles case of negative quantity values
        if (quantity < 0):
            raise ValueError("Quantity must be a non-negative integer value.")

        # Handles case of quantity exceeding currently existing quantity
        if (quantity > self.quantity):
            raise ValueError("Quantity to remove must not exceed remaining quantity of " + self.name + " left.")
        self.quantity -= quantity
        return self
