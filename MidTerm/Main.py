from HouseValueCalculator import House

running = True

while running:

  customerName = input("Please enter your name: ")
  print("Hi, %s, welcome to House Value Calculator:\n\nSelect the City\n\t1 Toronto\n\t2 Montreal\n\t3 to exit" %customerName)

  selection = int(input("Enter your selection: "))
  city = ""
  if selection == 1:
    city = "Toronto"
  elif selection == 2:
    city = "Montreal"
  elif selection == 3:
    break

  area = float(input("Enter the area: "))
  while area < 0:
    print("area must be > 0")
    area = float(input("Enter the area: "))

  numberOfRooms = int(input("Enter the number of rooms: "))
  while (numberOfRooms < 1) or (numberOfRooms > 5):
    print("number of rooms must be between 1 - 5")
    numberOfRooms = int(input("Enter the number of rooms: "))

  withBasement = input("are looking for house with basement y/n: ")

  if withBasement == "y":
    withBasement = True
  elif withBasement == "n":
    withBasement = False

  house = House(city, area, numberOfRooms, withBasement)

  print("Hi %s\n\tHouse value calculator:\n\tHouse information:\n\t%s\n\tEstimated price $%i" %(customerName, house.__str__(), house.estimatedPrice()))

  break
