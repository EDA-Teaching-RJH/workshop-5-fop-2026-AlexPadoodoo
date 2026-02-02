# Statement of Requirements:
# 1) Functional requirements: The code must only accept integers in the form of pence.
#    The program will then be able to use the amount given to calculate change
# 2) Non-Functional requirements: currently, if the user inputs a string into the program, it will break.
#    The program should be able to accept both strings and integers or atleast warn the user to only use integers. (Reliability Requirements)


import math

#prompts user to insert coin
print("**DISCLAIMER**")
print("**This machine only accepts 50p, 20p, 10p, 5p**")

print("Total Cost: 75p")

#calculates the amount due
amount_due = 75
while amount_due > 0:
    print(f"Amount Due: {amount_due}p")
    insert_coin = int(input("Please insert a coin: "))

#program checks if user has input the correct currency amount
    if insert_coin in [50, 20, 10, 5]:
        amount_due -= insert_coin

    else:
        print("Invalid coin. Please try again.")

# Calculates change required

change = abs(amount_due)
print("** Transaction Complete! **")
print(f"Your change is: {change}p")

# returns the exact amount of change using largest coin denominations first example

def calculate_change(change):
    coins = [50,20,10,5]
    



