import csv
class Item:
  def __init__(self, name, price):
        self.name = name
        self.price = price
  def getcatogery(self):
    pass
    catogeryquantity{}:
    with open('items.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      catogery = row['catogery']
      quantity = row['quantity']
      if catogery in catogeryquantity:
        catogeryquantity[getcatogery] = quantit
      else:
        catogeryquantity[getcatogery] = quantity  
        return catogeryquantity

    

    