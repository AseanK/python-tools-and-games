# If the bill is $150.00, split between 5 persons
# Each person should pay (150.00/5) * 1.12 = $33.6
# round the result to 2 decimal places

print("Welcome to the tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15 "))
people = int(input("How many people to split the bill?"))
bill_with_tip = (bill + (tip/100 * bill))
print(bill_with_tip)
bill_per_head = (bill_with_tip / people)
print("Bill per person is " "$" + str(bill_per_head))