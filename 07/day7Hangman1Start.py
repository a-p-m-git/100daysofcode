import random

word_list = ["ardvark", "baboon", "camel"]

#chosen_word = word_list[random.randint(0,len(word_list) -1)]
chosen_word = random.choice(word_list)
playerGuess = input("Guess a letter: ")

for letter in chosen_word:
   if playerGuess == letter:
       print("Right")
   else:
       print("Wrong")
   