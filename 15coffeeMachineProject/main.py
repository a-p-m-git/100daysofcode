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

playerMoney = {}

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
                return "True"
            else:
                return "Not enough coffee"
        else:
            return "Not enough water"
    elif customer_drink == "latte":
        if menuList[customer_drink]['ingredients']['water'] <= resourceList['water']:
            if menuList[customer_drink]['ingredients']['milk'] <= resourceList['milk']:
                if menuList[customer_drink]['ingredients']['coffee'] <= resourceList['coffee']:
                    return "True"
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
                        return "True"
                else:
                    return "Not enough coffee"
            else:
                return "Not enough milk"
        else:
            return "Not enough water"

def check_player_money(playerCoins,drink_cost):
    
    playerCoinTotal = 0
    
    for key in playerCoins:
        if key == "quarters":
            playerCoinTotal += (playerCoins["quarters"] * .25)
        elif key == "dimes":
            playerCoinTotal += (playerCoins["dimes"] * .10)
        elif key == "nickels":
            playerCoinTotal += (playerCoins["nickels"] * .05)
        else:
            playerCoinTotal += (playerCoins["pennies"] * .01 )
    
    return playerCoinTotal
        
    

while running:
    response = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
    if response != "report" and response !="off":
        print("Please insert coins: ")
        playerMoney["quarters"] = int(input("How many quarters? "))
        playerMoney["dimes"] = int(input("How many dimes? "))
        playerMoney["nickels"] = int(input("How many nickels? "))
        playerMoney["pennies"] = int(input("How many pennies? "))

    if response == 'espresso':
        print(f"Espresso - {MENU[response]['cost']}")
        
        if check_player_money(playerMoney,MENU[response]['cost']) < MENU[response]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            running = False

        resourcesAvailable = check_resources(resources,MENU,response)
        
        if resourcesAvailable == "True":
            playerChangeReturned = check_player_money(playerMoney,MENU[response]['cost']) - MENU[response]['cost']
            print(f"Here is ${playerChangeReturned} in change")
            resources["coffee"] -= MENU[response]["ingredients"]["coffee"]
            resources["water"] -= MENU[response]["ingredients"]["water"]
            print(f"Here is your {response}. Enjoy!")
        else:
            print(f"Sorry, there is {resourcesAvailable}")
            
    elif response == 'latte':
        print(f"Latte - {MENU[response]['cost']}")
        if check_player_money(playerMoney,MENU[response]['cost']) < MENU[response]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            running = False
        
        resourcesAvailable = check_resources(resources,MENU,response)
            
        if resourcesAvailable == "True":
            playerChangeReturned = check_player_money(playerMoney,MENU[response]['cost']) - MENU[response]['cost']
            print(f"Here is ${playerChangeReturned} in change")
            resources["coffee"] -= MENU[response]["ingredients"]["coffee"]
            resources["water"] -= MENU[response]["ingredients"]["water"]
            resources["milk"] -= MENU[response]["ingredients"]["milk"]
            print(f"Here is your {response}. Enjoy!")
        else:
            print(f"Sorry, there is {resourcesAvailable}")
    elif response == 'cappuccino':
        print(f"Cappucino - {MENU[response]['cost']}")
        if check_player_money(playerMoney,MENU[response]['cost']) < MENU[response]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            running = False
            
        resourcesAvailable = check_resources(resources,MENU,response)
            
        if resourcesAvailable == "True":
            playerChangeReturned = check_player_money(playerMoney,MENU[response]['cost']) - MENU[response]['cost']
            print(f"Here is ${playerChangeReturned} in change")
            resources["coffee"] -= MENU[response]["ingredients"]["coffee"]
            resources["water"] -= MENU[response]["ingredients"]["water"]
            resources["milk"] -= MENU[response]["ingredients"]["milk"]
            print(f"Here is your {response}. Enjoy!")
        else:
            print(f"Sorry, there is {resourcesAvailable}")
    elif response == 'report':
        resource_report(resources)
    elif response == 'off':
        running = False
        print("Exiting...")
    else:
        print(f"{response} is not a valid option.")