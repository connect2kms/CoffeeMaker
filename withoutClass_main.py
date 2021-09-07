MENU = {
    "esp": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "lat": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cap": {
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
    "money": 0
}


def check_inventory(coffee_type):
    inventory = MENU[coffee_type]
    is_avail = True
    for res in inventory["ingredients"]:
        if resources[res] < inventory["ingredients"][res]:
            is_avail = False
            print(f"Sorry there is not enough {res}.")

    return is_avail


def check_price(money_feed, coffee_type):
    resource_price = MENU[coffee_type]["cost"]
    if money_feed < resource_price:
        return -1
    else:
        return money_feed - resource_price


def make_coffee(coffee):
    inventory = MENU[coffee]
    for res in inventory["ingredients"]:
        resources[res] -= inventory["ingredients"][res]

    resources["money"] += MENU[coffee]["cost"]


def game_start():
    user_input = input("What would you like? (esp / lat / cap / report / off):  ")

    if user_input == 'off':
        return True

    if user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        return False

    available = check_inventory(user_input)

    if not available:
        return False

    print("Please insert coins.")
    user_quarters = int(input("how many quarters?:")) * 0.25
    user_dimes = int(input("how many dimes?:")) * 0.10
    user_nickles = int(input("how many nickles?:")) * 0.05
    user_pennies = int(input("how many pennies?:")) * 0.01

    money = user_quarters + user_dimes + user_nickles + user_pennies
    money = round(money, 2)

    money_refund = check_price(money, user_input)

    if money_refund == -1:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        make_coffee(user_input)
        print(f"Here is ${money_refund} in change.")
        print(f"Here is your {user_input} ☕️. Enjoy!")
        return False


end_of_game = False
while not end_of_game:
    end_of_game = game_start()
