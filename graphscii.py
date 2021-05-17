class Canvas(height, width):
  def __init__(self):
    self.height = height
    self.width = width
  def draw(figure):
    figure.display()
  
    
class Cursor(x, y):
  def __init__(self):
    self.x = x
    self.y = y
  def set(self):
    for i in range(x):
      print(" ", end="")
    for j in range(y):
      print(" ")
  def move(x, y):
    self.x = self.x + x
    self.y = self.y + y
    self.set()
  
class Rectangle(height, width, location):
  def __init__(self):
    self.height = height
    self.width = width
    self.location = location
    location.set()
  def display(self):
    for i in range(width):
      print("-", end="")
    for j in range(height):
      print("|", end="")
      for q in range(width - 2):
        print(" ", end="")
      print("|")
    for i in range(width):
      print("-", end="")
