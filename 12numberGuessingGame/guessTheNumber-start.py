#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

randomNumber = 0
response = ""
numOfGuess = 0


print(art.logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
randomNumber = random.randrange(1,100)
print(f"Psst, the correct answer is: {randomNumber}")

response = input("Choose a difficulty: Easy or Hard: ").lower()

if response == 'easy':
    numOfGuess = 10
else:
    numOfGuess = 5

while numOfGuess:
    print(f"You have {numOfGuess} attempts remaining to guess the number")
    
    response = int(input("Make a guess: "))
    if response == randomNumber:
        print(f"You got it! The number was: {randomNumber}")
        break
    elif response < randomNumber:
        print("Too Low!")
    else:
        print("Too High!")
    
    numOfGuess -= 1
    if numOfGuess == 0 :
        print("You've run out of guess. You lose!")

