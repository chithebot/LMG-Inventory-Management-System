# from item import item 
import csv
from user.py import User

class Main():
  
  def main_menu():
    with open('data.csv', mode ='r') as file:
      csvFile = csv.reader(file)
      for lines in csvFile:
            print(lines)
    
    
Main.main_menu()
