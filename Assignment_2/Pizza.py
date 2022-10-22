class Pizza:
  def __init__(self, size, price, pizzaNumber):
    self.size = size
    self.price = price
    self.pizzaNumber = pizzaNumber
  
  #getters
  def get_size(self):
    return self.size
  def get_price(self):
    return self.price
  def get_pizzaNumber(self):
    return self.pizzaNumber
  
  #setters
  def set_size(self, pizzaSize):
    if (pizzaSize == "Small") or (pizzaSize == "Medium") or (pizzaSize == "Large"):
      self.size = pizzaSize
    else:
      return False
  def set_price(self, pizzaPrice):
    self.price = pizzaPrice
  def set_pizzaNumber(self, number):
    self.pizzaNumber = number

  def total(self):
    if (self.pizzaNumber < 3) and (self.pizzaNumber > 0):
      return self.price * self.pizzaNumber
    elif self.pizzaNumber >= 3:
      return (self.price * self.pizzaNumber) - (self.price * self.pizzaNumber)*0.15