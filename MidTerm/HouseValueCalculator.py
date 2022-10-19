import numbers
from random import randint

class House:
  def __init__(self, city, area, numberOfRooms, basement):
    self.city = city
    self.area = area
    self.numberOfRooms = numberOfRooms
    self.basement = basement
  
  def estimatedPrice(self):
    estPrice = 0
    if self.numberOfRooms == 1:
      estPrice = randint(500, 550)
    elif self.numberOfRooms == 2:
      estPrice = randint(600, 750)
    elif self.numberOfRooms >= 3:
      estPrice = randint(750, 950)

    return estPrice*1000
  
  def __str__(self):
    withBasement = "without"
    if self.basement == True:
      withBasement = "with"
    return ("City: %s area %.1f Number of Rooms: %d %s basement" %(self.city, self.area, self.numberOfRooms, withBasement))

