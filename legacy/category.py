class Catogory:
  
  def __init__(self, name):
    self.name = name
    self.item = []
    pass

  def add_item(self, item):  
    self.item.append(item)
    
  def create_category(self, name: str):
      """Create a new category."""
      self.name = name

  def display(self):
      """Display the category."""
      print(f"Category: {self.name}")