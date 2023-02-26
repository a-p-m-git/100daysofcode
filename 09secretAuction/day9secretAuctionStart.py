import art
import os

def highest_bid(bidDictionary):
    highest = 0
    highestBidder = ""

    print(bidDictionary)
    input()

    for key in bidDictionary:
        aBid = int(bidDictionary[key])
        print(key)
        if  aBid > highest:
            print(f"{key} bid of {bidDictionary[key]} is greater than {highest}")
            highest = aBid
            highestBidder = key
        else:
            print(f"{key} bid of {bidDictionary[key]} is less than {highest}")

    print(f"The winner is {highestBidder} with a bid of ${highest}")

running = True
playerBids = {}

while running:

    print(art.logo)

    name = input("What is your name? ")
    bid = int(input("What is your bid?"))

    playerBids[name] = bid  
    print(playerBids[name])
    otherPlayers = input("Are there any other bidders? Type 'Yes' or 'No'\n").lower()
    
    if otherPlayers == "no":
        running = False
    else:
        os.system("clear")

    #print(playerBids)

highest_bid(playerBids)