#Hao Cui has claimed this spot. Do not touch this file
import csv

#the 3 lines below are for asking user to input usernamd and password
#in the main menu.

#create_username = input("Create Username: ")
#create_password = input("Create Password: ")
#person1 = User(create_username, create_password) 

class User:

  #user createion
  def __init__(self, user_name, password):
    self.create_user_name = user_name.lower()
    self.create_password = password

    #TODO: 
    #1. Check if user_name already exist in the file, if so print some error.
    # we can check all the odd numbers of elements for usernames
    #2. (BONUS): limit characters of username and password.
    # Force minimum special characters and non repeating characters
    try:
      with open("user.csv", mode = "a") as file:
        writer = csv.writer(file)
        writer.writerow([self.create_user_name , self.create_password])
    except ValueError:
      print("test")

  #user authentication

  #def auth(user_name, password):
    #TODO: 
  #1. Check whether user_name exist in the user.csv file, if so then say user_name DNE
  #2. If user_name exists in user.csv file, then check the very next element to match
  #. the password.