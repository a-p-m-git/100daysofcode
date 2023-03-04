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
    "money":0
}

running = True


def resource_report(resourceList):
    print(f"Water: {resourceList['water']}ml")
    print(f"Milk: {resourceList['milk']}ml")
    print(f"Coffee: {resourceList['coffee']}mg")
    print(f"Money: ${resourceList['money']} ")

def check_resources(resourceList,menuList,customer_drink):
    
    if customer_drink == "espresso":
        if menuList[customer_drink]['ingredients']['water'] <= resourceList['water']:
            if menuList[customer_drink]['ingredients']['coffee'] <= resourceList['coffee']:
                return True
            else:
                return "Not enough coffee"
        else:
            return "Not enough water"
    elif customer_drink == "latte":
        if menuList[customer_drink]['ingredients']['water'] <= resourceList['water']:
            if menuList[customer_drink]['ingredients']['milk'] <= resourceList['milk']:
                if menuList[customer_drink]['ingredients']['coffee'] <= resourceList['coffee']:
                    return True
                else:
                    return "Not enough coffee"
            else:
                return "Not enough milk"
        else:
            return "Not enough water"   
    elif customer_drink == "cappuccino":
        if menuList[customer_drink]['ingredients']['water'] <= resourceList['water']:
            if menuList[customer_drink]['ingredients']['milk'] <= resourceList['milk']:
                if menuList[customer_drink]['ingredients']['coffee'] <= resourceList['coffee']:
                        return True
                else:
                    return "Not enough coffee"
            else:
                return "Not enough milk"
        else:
            return "Not enough water"


while running:
    response = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print("Please insert coins: ")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    if response == 'espresso':
        print(f"Espresso - {MENU[response]['cost']}")
        print(check_resources(resources,MENU,response))
    elif response == 'latte':
        print(f"Latte - {MENU[response]['cost']}")
        print(check_resources(resources,MENU,response))
    elif response == 'cappuccino':
        print(f"Cappucino - {MENU[response]['cost']}")
        print(check_resources(resources,MENU,response))
    elif response == 'report':
        resource_report(resources)
    elif response == 'off':
        running = False
        print("Exiting...")
    else:
        print(f"{response} is not a valid option.")