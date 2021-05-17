class Canvas:
  def __init__(self, height, width):
    self.height = height
    self.width = width
  def draw(self, figure):
    figure.display()
  
    
class Cursor:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def set(self):
    for j in range(self.y):
      print(" ")
    for i in range(self.x):
      print(" ", end="")
  def move(self, x, y):
    self.x = self.x + x
    self.y = self.y + y
    self.set()
  
class Rectangle:
  def __init__(self, height, width, location):
    self.height = height
    self.width = width
    self.location = location
    location.set()
  def display(self):
    for i in range(self.width):
      print("-", end="")
    print()
    for j in range(self.height):
      for i in range(self.location.x):
        print(" ", end="")
      print("|", end="")
      for q in range(self.width - 2):
        print(" ", end="")
      print("|")
    for i in range(self.location.x):
        print(" ", end="")
    for i in range(self.width):
      print("-", end="")
    print()
