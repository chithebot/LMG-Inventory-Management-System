import csv

import list_database as ldb


class CategoryDatabase(ldb.ListDatabase):
        
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
