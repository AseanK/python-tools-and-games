def add(num1, num2):
    print(num1 + num2)
    return num1 + num2

def subtract(num1, num2):
    print(num1 - num2)
    return num1 - num2

def multiply(num1, num2):
    print(num1 * num2)
    return num1 * num2

def divide(num1, num2):
    print(num1 / num2)
    return num1 / num2

conti = True
num1 = int(input("Enter the first number \n"))
while conti:
    sym = input("'+', '-', '*', '/'\n")
    num2 = int(input("Enter the second number \n"))
    if sym == "+":
       num1 =  add(num1, num2)
    if sym == "-":
        num1 =  subtract(num1, num2)
    if sym == "*":
        num1 =  multiply(num1, num2)
    if sym == "/":
        num1 =  divide(num1, num2)
    contiInput = input("Continue? 'y'es or 'n'o\n")
    if contiInput == "n":
        conti = False