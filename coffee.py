import math

#prompts user to insert coin
print("**DISCLAIMER**")
print("**This machine only accepts 50p, 20p, 10p, 5p**")

insert_coin = int(input("Please insert a coin: "))
print("Total cost: 75p")

#program checks if user has enough money
if insert_coin ==75:
    print("Thank you for your service! ")

# Calculates change required

elif insert_coin >75:
    change = insert_coin - 75
    print(f"Your change is: {change}p")
