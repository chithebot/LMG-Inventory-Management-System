import csv

import list_database as ldb


class CategoryDatabase(ldb.ListDatabase):
    """ This class is a database for categories.
    """
    __doc__ += ('\n' + ldb.ListDatabase.__doc__)

    """
    This function reads the category data from the file that is stored
    in the current CategoryDatabase object. The data is read into the 
    database container of this object.

    Args:
        self (CategoryDatabase) : the current CategoryDatabase object

    Raises:
        IOError: Raised if file could not be opened
    """
    def readData(self):
        
        try:

            # Opening file for reading
            with open(self.filename, mode='r', newline='\n') as csvfile:

                reader = csv.reader(csvfile, delimiter=',')
                
                # Reading data from csv file
                next(reader)        # skips header
                for row in reader:
                    category = row[0]
                    self.db.append(category)

        # Handles case of failure to open file
        except IOError as e:
            print("File could not be opened: ", e)


    """
    This function saves the category data from the database container, of
    the current CategoryDatabase object, into the file located at the filename
    stored in this object.

    Args:
        self (CategoryDatabase) : the current CategoryDatabase object

    Raises:
        IOError: Raised if file could not be opened
    """
    def saveData(self):

        try:
            
            # Opening file for reading and appending
            with open(self.filename, mode='w', newline='\n') as csvfile:

                writer = csv.writer(csvfile, delimiter=',')

                # Writing data from database into csv file
                header = ["categories"]
                writer.writerow(header)
                for row in self.db:
                    writer.writerow([row])

        # Handles case of failure to open file
        except IOError as e:
            print("File could not be opened: ", e)


    """
    This function sorts the categories. If reverse is set then the
    categories will be sorted in the reverse order. Reverse is set
    to False as its default configuration.

    Args:
        self (CategoryDatabase) : the current CategoryDatabase object
        reverse (bool)          : an indicator to sort in reverse order
    """
    def sort(self, reverse=False):
        self.db.sort(reverse=reverse)