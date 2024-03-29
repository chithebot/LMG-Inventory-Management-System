from user import Create_User, User


class Main():
    
    def remote(self,option):
        if option == -10:
            print("--Login/Logout Interface--")
        elif option == 1: 
            print("--Create new user Interface--")
        elif option == 2: 
            print("--Create Item Interface--")
        elif option == 3:
            print("--Create Category Interface--")
        elif option == 4: 
            print("--Create Search Interface--")

    
    def main_menu(self):
        user_input=-10
        self.remote(user_input)
        while exit !=0:
            print("------ Main Menu ------")
            print("1. Create New User ")
            print("2.) Enter Item Interface  ")
            print("3.) Enter Category Interface")
            print("4.) Search")
            print("5.) Logout and Exit")
            
            user_input = int(input("Enter your choice (0-5):"))
            print("\n")
            if user_input == 5:
                print("Successfully Logged Out Of System ")
                break
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


Main().main_menu()
