import csv

import dict_database as ddb


class UserDatabase(ddb.DictDatabase):
    """ This class is a database for users.
    """
    __doc__ += ('\n' + ddb.DictDatabase.__doc__)


    """
    This function saves the user data from the database container, of
    the current UserDatabase object, into the file located at the filename
    stored in this object.

    Args:
        self (UserDatabase) : the current UserDatabase object

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
                    username = row[1]
                    password = row[2]
                    self.db[username] = [name, password]

        # Handles case of failure to open file
        except IOError as e:
            print("File could not be opened: ", e)


    """
    This function saves the user data from the database container, of
    the current UserDatabase object, into the file located at the filename
    stored in this object.

    Args:
        self (UserDatabase) : the current UserDatabase object

    Raises:
        IOError: Raised if file could not be opened
    """
    def saveData(self):

        try:
            
            # Opening file for reading and appending
            with open(self.filename, mode='w', newline='\n') as csvfile:

                writer = csv.writer(csvfile, delimiter=',')

                # Writing data from database into csv file
                header = ["name", "username", "password"]
                writer.writerow(header)
                for row in self.db:
                    writer.writerow([self.db[row][0], row, self.db[row][1]])

        # Handles case of failure to open file
        except IOError as e:
            print("File could not be opened: ", e)