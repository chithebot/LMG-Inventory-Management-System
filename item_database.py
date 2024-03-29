import csv

import item
import list_database as ldb


class ItemDatabase(ldb.ListDatabase):
    """ This class is a database for items.
    """
    __doc__ += ('\n' + ldb.ListDatabase.__doc__)
    

    """
    This function reads the item data from the file that is stored
    in the current ItemDatabase object. The data is read into the 
    database container of this object.

    Args:
        self (ItemDatabase) : the current ItemDatabase object

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
                    name = row[0]
                    sku = int(row[1])
                    category = row[2]
                    quantity = int(row[3])
                    self.db.append(item.Item(name, sku, category, quantity))

        # Handles case of failure to open file
        except IOError as e:
            print("File could not be opened: ", e)


    """
    This function saves the item data from the database container, of
    the current ItemDatabase object, into the file located at the filename
    stored in this object.

    Args:
        self (ItemDatabase) : the current ItemDatabase object

    Raises:
        IOError: Raised if file could not be opened
    """
    def saveData(self):

        try:
            
            # Opening file for reading and appending
            with open(self.filename, mode='w', newline='\n') as csvfile:

                writer = csv.writer(csvfile, delimiter=',')

                # Writing data from database into csv file
                header = ["name", "sku", "category", "quantity"]
                writer.writerow(header)
                for row in self.db:
                    writer.writerow([row.name, row.sku, row.category, row.quantity])

        # Handles case of failure to open file
        except IOError as e:
            print("File could not be opened: ", e)
    