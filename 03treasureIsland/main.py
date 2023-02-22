running = True

print("Welcome to Treasure Island\nYour Mission is to find the treasure")

while running:
    response = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
    if response == "left":
        response = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")
        if response == "wait":
            response = input("You arrive at the island unharmed. THere is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
            if response == "yellow":
                print("YOU ARE THE WEINER!!")
                running = False
            elif response == "blue":
                print("You are eaten by beasts. Game Over!")
                running = False
            else:
                print("You ded, Game Over!")
                running = False
        else:
            print("You have been attacked by a trout. Game Over!")
            running = False
    else:
        print("You fall into a hole. Game Over!")
        running = False
        
        