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