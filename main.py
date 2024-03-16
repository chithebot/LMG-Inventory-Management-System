import csv
from user import User

class Main():
  
  def main_menu(self):
    exit=0
    self.login_logout()
    while exit !=0:
      print("----Welcome to the main menu---")
      print("0. Create New User ")
      print("1.) Logout")
      print("2.) Enter Item Interface  ")
      print("3.) Enter User Interface  ")
      print("4.) Enter Category Interface")
      print("5.) Enter Display Interface")
      print("6.) Enter Sort Interface")
      print("7.) Enter Search Interface")
      print("8.) Enter Stock-Alert Interface")
      # user_input = input("Enter input")
      
    
  # def access_item_category_data():
  #     with open('data.csv', mode ='r') as file:
  #     csvFile = csv.reader(file)
  #     for lines in csvFile:
  #           print(lines)

  #def create_user(self):
  #  create_username = input("Create Username: ")
  #  create_password = input("Create Password: ")
  #  user1 = Create_User(create_username, create_password)

  #def login(self):
  #  login_username = input("Login Username: ")
  #  login_password = input("Login Password: ")
  #  logged_user = User(login_username, login_password)    
  #  print("message after login sucessful, this line should not print if login has failed")


    
    
Main().main_menu()
