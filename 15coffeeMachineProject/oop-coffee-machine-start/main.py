from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


new_menu = Menu()
new_coffeemaker = CoffeeMaker()
new_moneymachine = MoneyMachine()

running = True


while running:
    
    response = input("What would you like? (espresso,latte,cappuccino):").lower()
                    
    if response == "off":
        running = False        
    elif response == "report":
        new_coffeemaker.report()
    elif response == "espresso":
        if new_coffeemaker.is_resource_sufficient(response):
            new_moneymachine.process_coins():
                if new_moneymachine.make_payment(menu) 
    elif response == "latte":
        if new_coffeemaker.is_resource_sufficient(response):
            pass
    elif response == "cappuccino":
        if new_coffeemaker.is_resource_sufficient(response):
            pass   
    else:
        print(f"{response} is not a valid option")




