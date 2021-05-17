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
    self.set()
  def set(self):
    for i in range(x):
      print(" ", end="")
    for j in range(y):
      print(" ")
  def move(x, y):
    self.x = self.x + x
    self.y = self.y + y
    self.set()
  
