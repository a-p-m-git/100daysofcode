import random

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

word_list = ["ardvark", "baboon", "camel"]
display_list = []
running = True
playerLife = 6

#chosen_word = word_list[random.randint(0,len(word_list) -1)]
chosen_word = random.choice(word_list)



#populate list with underscores
for i in range(0,len(chosen_word)):
    display_list.append("_")

#ask player to guess a letter

print(f"Psst, the solution is {chosen_word}")
print(stages[playerLife])
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
        playerLife -= 1
                
    if "_" not in display_list:
        running = False
        print("You win!")
        print(stages[playerLife])
        print(display_list)
    elif playerLife <= 0:
        running = False
        print("You ded!")
        print(stages[playerLife])
        print(display_list)
    else:
        print(stages[playerLife])
        print(f"{playerLife} / {playerGuessHits}")
        print(display_list)
    
    #try:
    #    display_list.index("_")           
    #except ValueError:
    #    print("You won!")
    #    print(display_list)
    #    running = False