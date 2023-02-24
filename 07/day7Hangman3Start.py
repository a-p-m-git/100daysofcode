import random

word_list = ["ardvark", "baboon", "camel"]
display_list = []
running = True
#chosen_word = word_list[random.randint(0,len(word_list) -1)]
chosen_word = random.choice(word_list)

#populate list with underscores
for i in range(0,len(chosen_word)):
    display_list.append("_")

#ask player to guess a letter

print(f"Psst, the solution is {chosen_word}")
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
    
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == playerGuess:
            display_list[i] = letter
    print(display_list)
    try:
        display_list.index("_")           
    except ValueError:
        print("You won!")
        print(display_list)
        running = False