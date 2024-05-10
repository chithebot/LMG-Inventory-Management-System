import csv

import dict_database as ddb
import tools
import user


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
        IOError    : Raised if file could not be opened
        ValueError : Raised if strings cannot be converted to integers.
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

                    security_question = None
                    if row[3] != "None":
                        security_question = int(row[3])

                    security_question_ans = None
                    if row[4] != "None":
                        security_question_ans = row[4]
                    
                    last_login_attempt = None
                    if row[5] != "None":
                        last_login_attempt = tools.stringToDatetime(row[5])
                    
                    login_attempts = int(row[6].strip())
                    self.db[username] = user.User(name, username, password, security_question,
                                                  security_question_ans, last_login_attempt, login_attempts)

        # Handles case of failure to open file
        except IOError as e:
            print("File could not be opened: ", e)
        
        # Handles case of login attempts not being able to be converted to int
        except ValueError as e:
            print("login_attempts field could not be converted to int: ", e)


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
                header = ["name", "username", "password", "security_question",
                          "security_question_ans", "last_login_attempt", "login_attempts"]
                writer.writerow(header)
                for row in self.db:
                    usr = self.db[row]
                    writer.writerow([usr.name, usr.username, usr.password, usr.security_question,
                                    usr.security_question_ans, str(usr.last_login_attempt), usr.login_attempts])

        # Handles case of failure to open file
        except IOError as e:
            print("File could not be opened: ", e)