#main.py
import csv
import os
from user import Create_User, User


class Main():
    
    def remote(self,option):
        if option == -10:
         print("1")
        elif option == -1: 
            print("--Create new user Interface--")
        elif option == 2: 
            print("--Create Item Interface--")
            
        elif option == 3:
            print("--Create Category Interface--")
        elif option == 4: 
            print("--Create Search Interface--")
    def item_interface(self):
      while True:
          print("--Item Interface--")
          print("1.) Create Item")
          print("2.) Remove Item")
          print("3.) Search Item")
          print("4.) Exit Item Interface")
          choice = int(input("Enter your choice (1-4): "))
          if choice == 1:
              self.create_item()
          elif choice == 2:
              
              self.remove_item()
          elif choice == 3:
              pass
              # self.search_item()
          elif choice == 4:
              break
          else:
              print("Invalid choice. Please enter a number between 1 and 4.")
    
    def main_menu(self):
        user_input=100
        print("1.) Login")
        print("2.) Create new user")
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
          self.remote(-10)
        elif user_input == 2:
          self.remote(-1)
        user_input = 100
        while user_input!= 4:
            print("------ Main Menu ------")
            print("1.) Enter Item Interface  ")
            print("2.) Enter Category Interface")
            print("3.) Search")
            print("4.) Logout and Exit")
            
            user_input = int(input("Enter your choice (0-4):"))
            print("\n")
            if user_input == 4:
                print("Successfully Logged Out Of System ")
                break
            elif user_input == 1:
                self.item_interface()
          
            self.remote(user_input)
        if user_input == -10:  # New condition for sorting items by quantity
          item_db = ItemDatabase("item_data.csv")
          item_db.readData()
          item_db.sortItemsByQuantity()
          print("Items sorted by quantity:")
          item_db.displayItems()
        elif user_input == 1:
          self.item_interface()
        elif user_input == 2:
          self.display_categories()  # Call display_categories method
        elif user_input == 3:
          self.search_interface()
        else:
          self.remote(user_input)
          
    def create_user(self):
        print("Enter your login credential:\n")
        create_username = input("Create Username: ")
        create_password = input("Create Password: ")
        user1 = Create_User(create_username, create_password)


    def login(self):
        login_username = input("Login Username: ")
        login_password = input("Login Password: ")
        logged_user = User(login_username, login_password)    
        print("message after login sucessful, this line should not print if login has failed")
        
  # def access_item_category_data():
  #     with open('data.csv', mode ='r') as file:
  #     csvFile = csv.reader(file)
  #     for lines in csvFile:
  #           print(lines)
    def display_categories(self):
      """Display categories."""
      category_db = CategoryDatabase("category_data.csv")
      category_db.readData()
      print("Categories:")
      for category in category_db.db:
          print(category)




    def create_item(self):
       item_name = input("Enter item name: ")
       sku = input("Enter SKU: ")
       category = input("Enter category: ")
       quantity = input("Enter quantity: ")

       data_folder = 'data'
       file_path = os.path.join(data_folder, 'item_data.csv')
       with open(file_path, mode='a', newline='') as file:
           writer = csv.writer(file)
           writer.writerow([item_name, sku, category, quantity])
           print("Item created successfully!")
    def remove_item(self):
      item_name = input("Enter item name to remove: ")

      data_folder = 'data'
      file_path = os.path.join(data_folder, 'item_data.csv')

      # Read the existing data
      with open(file_path, mode='r', newline='') as file:
          reader = csv.reader(file)
          rows = list(reader)

      # Remove the item if it exists
      removed = False
      with open(file_path, mode='w', newline='') as file:
          writer = csv.writer(file)
          for row in rows:
              if row[0] == item_name:
                  print(f"Item '{item_name}' removed successfully!")
                  removed = True
              else:
                  writer.writerow(row)
          if not removed:
              print(f"Item '{item_name}' not found.")

Main().main_menu()
