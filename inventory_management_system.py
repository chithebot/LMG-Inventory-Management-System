import system


class InventoryManagementSystem:
    """ This class is the inventory management system.
    """

    """
    This function runs the inventory management system application.

    Args:
        self (InventoryManagementSystem) : the current Database object
    """
    def run(self):

        # Defining file locations of databases
        folder = "data/"
        ext = ".csv"
        cdbfile = folder + "category_data" + ext
        idbfile = folder + "item_data" + ext
        udbfile = folder + "user_data" + ext

        # Runs the system's programs
        ims = system.System(cdbfile, idbfile, udbfile)

        # Running the inventory management system
        while not ims.exit:
            ims.update()