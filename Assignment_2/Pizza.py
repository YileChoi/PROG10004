class Pizza:
  def __init__(self, size, price, pizzaNumber):
    self.size = size
    self.price = price
    self.pizzaNumber = pizzaNumber
  
  @property
  def get_size(self):
    return self.size
