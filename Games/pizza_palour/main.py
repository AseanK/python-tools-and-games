from utils import package_installer
package_installer.install_dependencies()

# Congratulations! you just got a job at python pizza,
# Your first job is to build an automatic pizza orderin system
# Based on user's order, work out the final bill

# Pepperoni for small pizza = $2
# Pepperoni for large and medium pizza = $3
# Extra cheese for any size = $1

# Example input:
# size = L
# add_pepperoni = "Y"
# extra_cheese = "N"

greetings = ("Welcome to Python Pizza ")
name = (input("What is your name please? "))
print(greetings + name + "!")

# Small_pizza = 15 #small_pizza
# Medium_pizza = 20 #medium_pizza
# Large_pizza = 25 #Large_pizz


order = (input("What size of pizza would you like to have?\nWe have the following options:\nS for Small Pizza\nM for Medium-sized Pizza\nand L for Large pizza? "))
print(order)

if order == "S":
    bill = 15
    print("Please pay $15 for yor order")
elif order == "M":
    bill = 20
    print("Please pay $20 for yor order")
elif order == "L":
    bill = 25
    print("Please pay $25 for your order")

wants_pepperoni = (input("Do you want pepperoni Y or N ? "))
if wants_pepperoni == "Y":
    size_pepperoni = (input("Which size of pepperoni do you want: Small, Medium or Large? "))
    print(size_pepperoni + "! " + "That's Excellent " + name)
    if size_pepperoni == "Small":
        bill += 2
        print(f"Your total bill is ${bill}")
    if size_pepperoni == "Medium":
        bill += 3
        print(f"Your total bill is ${bill}")
    if size_pepperoni == "Large":
        bill += 3
        print(f"Your total bill is ${bill}")
else:
    print(f"Thank you for your order {name}; Your bill remains {bill}.\nPlease pay ${bill} to validate your order!")

extra_cheese = (input("Do you want extra cheese Y or N?"))
if extra_cheese == "Y":
    bill += 1
    print(f"Your Total bill is ${bill}")
else:
    print(f"Thank you for your order {name},\n Please pay {bill} to validate your order!")