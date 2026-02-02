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
