############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():

    playerScore = 0 
    computerScore = 0
    playerCards = []
    computerCards = []

    response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    if response == 'y':
        print(art.logo)
        while deal(playerCards,computerCards):
            pass
        return True 
    else:
        return False

def deal(playerCards,computerCards):
    
    playing = True

    for i in range(2):
        playerCards.append(random.choice(cards))
        computerCards.append(random.choice(cards))
        
    print(f"Your cards: {playerCards}, finalScore: {sum(playerCards)}")
    print(f"Computer's first card: {computerCards[0]}")
    
    while playing:

        response = input("Type 'y' to get another card, type 'n' to pass ").lower()

        if response == 'y' and sum(playerCards) <= 21:
            playerCards.append(random.choice(cards))
            computerCards.append(random.choice(cards))
        
            print(f"Your cards: {playerCards}, finalScore: {sum(playerCards)}")
            print(f"Computer's first card: {computerCards[0]}")
        else:
            print(f"Your final hand: {playerCards}, Your final score: {sum(playerCards)}")
            print(f"Computer's final hand: {computerCards}, final score: {sum(computerCards)}")
            if (sum(playerCards)) > (sum(computerCards)):
                print("You are da WEINER!")
            else:
                print("Computers Wins!")
                    
        if int(sum(playerCards)) > 21 :
            print("You went over. You lose")
            playing = False
            return False
        elif sum(computerCards) > 21:
            print("The computer went over. You WIN!")
            playing = False
            return False
        
        
while blackjack():
    blackjack()
