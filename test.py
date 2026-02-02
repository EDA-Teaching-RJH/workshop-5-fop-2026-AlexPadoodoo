# Statement of Requirements:
# 1) Functional requirements: The code must only accept integers in the form of pence.
#    The program will then be able to use the amount given to calculate change
# 2) Non-Functional requirements: currently, if the user inputs a string into the program, it will break.
#    The program should be able to accept both strings and integers or atleast warn the user to only use integers. (Reliability Requirements)


import math

#prompts user to insert coin
print("**DISCLAIMER**")
print("**This machine only accepts 50p, 20p, 10p, 5p**")
print("-----------------------------------")

# Asks user what type of drink they want
def select_drink():
    print("Welcome to the Coffee Machine!")
    drink = input("What type of drink would you like? (espresso/latte/cappuccino): ").lower()

# Sets prices for each drink
    espresso_price = 50
    latte_price = 60
    cappuccino_price = 75

# Determines cost based on user selection
    if drink == "espresso":
        print("You have selected an Espresso. That will be 50p.")
        cost = espresso_price
    elif drink == "latte":
        print("You have selected a Latte. That will be 60p.")
        cost = latte_price
    elif drink == "cappuccino":
        print("You have selected a Cappuccino. That will be 75p.")
        cost = cappuccino_price
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
    return cost
cost = select_drink()




print(f"Total Cost: {cost}p")

#calculates the amount due
amount_due = cost
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
    change_coins = []
    for coin in coins:
        while change >= coin:
            change -= coin
            change_coins.append(coin)
    return change_coins
change_coins = calculate_change(change)
print("Your change is given as: ")
for coin in change_coins: 
    print(f"{coin}p")



