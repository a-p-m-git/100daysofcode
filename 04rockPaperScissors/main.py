import random

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    ____________
---'   ____)____) )
            ____) )
          ______)
       __________)
      (____)
---.__(___)
'''

running = True


while running:
    
    response = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    
    if response == 0:
        print(rock)
    elif response == 1:
        print(paper)
    else:
        print(scissors)
        
    computerChoice = random.randint(0,2)
    
    print(f"Computer chose:\n")
    
    if computerChoice == 0:
        print(rock)
    elif computerChoice == 1:
        print(paper)
    else:
        print(scissors)


    if response == computerChoice:
        print("It's a draw")
    elif response >= 3 or response < 0:
        print("You typed an invalid numbers, you lose!")
    elif (response == 0 and computerChoice == 2) or (response == 2 and computerChoice == 1) or (response == 1 and computerChoice == 0):
        print("You win!")
    else:
        print("You lose!")

    


    
    