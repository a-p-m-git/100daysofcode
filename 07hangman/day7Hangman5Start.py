import random
import os
import hangman_art
import hangman_words

stages = ['''
   +---+
   |   |    
   0   |
  /|\  |
   |   |
  / \  |   
========''', '''
   +---+
   |   |    
   0   |
  /|\  |
   |   |
  /    |   
========''', '''
   +---+
   |   |    
   0   |
  /|\  |
   |   |
       |   
========''', '''
   +---+
   |   |    
   0   |
  / \  |
       |
       |   
========''','''
   +---+
   |   |    
   0   |
  /    |
       |
       |   
========''','''
   +---+
   |   |    
   0   |
       |
       |
       |   
========''','''
   +---+
   |   |    
       |
       |
       |
       |   
========''']

#word_list = ["ardvark", "baboon", "camel"]
display_list = []
running = True
playerLife = 6
playerGuessHistory = []

#chosen_word = word_list[random.randint(0,len(word_list) -1)]
chosen_word = random.choice(hangman_words.word_list)

#populate list with underscores
for i in range(0,len(chosen_word)):
    display_list.append("_")

#ask player to guess a letter

#print(f"Psst, the solution is {chosen_word}")

print(hangman_art.logo)

print(stages[playerLife] + "\n")
print(display_list)

#a = 0 

#for letter in chosen_word:
#   if playerGuess == letter:
#       print("Right")
#       display_list[a] = playerGuess
#   else:
#       print("Wrong")
#   a +=1

while running:
    
    playerGuess = input("Guess a letter: ").lower()
    playerGuessHits = 0
    
    if playerGuess not in playerGuessHistory:
        
        playerGuessHistory.append(playerGuess)

        for i in range(len(chosen_word)):
            
            letter = chosen_word[i]
            #print(f"Current Position: {i}\n Current Letter: {letter}\n Guessed Letter: {playerGuess}")
            if letter == playerGuess:
                #print(f"{playerGuess} - {letter} found")
                display_list[i] = letter
                playerGuessHits += 1
            #else:
                #print(f"{playerGuess} - {letter} not found")
        
        if playerGuessHits == 0:
            print(f"{playerGuess} is not in the word")
            playerLife -= 1
                    
        if "_" not in display_list:
            running = False
            os.system("clear")
            print(stages[playerLife])
            print(display_list)
            print("You win!")
        elif playerLife <= 0:
            running = False
            os.system("clear")
            print(stages[playerLife])
            print(display_list)
            print("You ded!")
        else:
            os.system("clear")
            print(stages[playerLife])
            print(display_list)
            print(f"{playerLife} / {playerGuessHits}")
    else:
        os.system("clear")
        print(stages[playerLife])
        print(display_list)
        print(f"You already guessed: {playerGuess}")
    #try:
    #    display_list.index("_")           
    #except ValueError:
    #    print("You won!")
    #    print(display_list)
    #    running = False