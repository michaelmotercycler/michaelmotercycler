MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 2. Check for sufficient resources
def sufficent_resources(order_ingredients):
    #Compare order_ingredients with resources
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry. Insufficient resources.")
            return False
    else:
        return True
            
def enter_coins():
    print("PLease enter coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
    
def process_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit =+ drink_cost
        return True
    else:
        print("Sorry. Not enough money. Money refunded.")
        return False

def make_coffee(choice, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")
    

    

# TODO: 1. Check what the customer would like 
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    if choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Profit: ${profit}")
        
    elif choice == "off":
        is_on = False
        
    else: 
        drink = MENU[choice]
        if sufficent_resources(drink["ingredients"]):
            payment = enter_coins()
            if process_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        
    
    
    
    
    


    


