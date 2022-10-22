from User import User
from Pizza import Pizza

asdf = User("Yile", "test email", "test address")

name = input("What is your name?: ")
email = input("What is your email address?: ")
address = input("What is your address?: ")
user_info = User(name, email, address)

size = ""
pizzaNumber = 0
price = 0

user_pizza = Pizza(size, price, pizzaNumber)
while True:
  size = input("What size Pizza would you like? (Small/Medium/Large): ")
  if size == "Small":
    user_pizza.set_price(10)
    user_pizza.set_size("Small")
    break
  elif size == "Medium":
    user_pizza.set_price(12)
    user_pizza.set_size("Medium")
    break
  elif size == "Large":
    user_pizza.set_price(15)
    user_pizza.set_size("Large")
    break
  else:
    print("wrong input. Please enter again.")
    size = input("What size Pizza would you like? (Small/Medium/Large): ")

print("One Pizza of this size is $%.1f" %user_pizza.get_price())
pizzaNumber = int(input("How many Pizzas of this size would you like?: "))
user_pizza.set_pizzaNumber(pizzaNumber)

print("You have ordered %i %s pizzas" %(user_pizza.get_pizzaNumber(), user_pizza.get_size()))

print("Your total is, $ %.1f" %user_pizza.total())
print("Order will be delivered to Tim at %s" %user_info.address)
print("Receipt will be emailed to %s" %user_info.email)