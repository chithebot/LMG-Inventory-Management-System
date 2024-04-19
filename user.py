#user.py
#Hao Cui has claimed this spot. Do not touch this file
import csv
import sys

class Create_User:

  #user createion
  def __init__(self, user_name, user_password):
    self.create_user_name = user_name.lower()
    self.create_password = user_password
    with open("user.csv") as file:
      if self.create_user_name in file.read(): #check if username is in the file
        print(f"The username {self.create_user_name} already exists!")
      else:
        with open("user.csv", mode = "a") as file:
          writer = csv.writer(file)
          writer.writerow([self.create_user_name , self.create_password])
          print("Your Account has been created successfully!")
          print(f"Your Username is: {self.create_user_name} \nYour Password is: {self.create_password}")

class User:
  def __init__(self, user_name, user_password):
    with open("user.csv") as file:
      account = [user_name, user_password]
      reader = csv.reader(file)
      for i in reader:
        if user_name in i and account == i:
          print("Login successful!")
          break
        else:
          print("Login Failed!")
          sys.exit(1)
