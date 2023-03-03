import os
import art
import game_data
import random

game_choices = {"A":[],"B":[]}

def random_entry(data_dictionary):
    return random.choice(data_dictionary)

def print_entry(entry):
    print(f"{entry['name']}, {entry['description']}, from {entry['country']} - {entry['follower_count']}")

def compare_follower_counts(dictionaryA,dictionaryB):
    if dictionaryA["follower_count"] > dictionaryB["follower_count"]:
        return "A"
    elif dictionaryA["follower_count"] < dictionaryB["follower_count"]:
        return "B"

def game():
    os.system("cls")
    running = True
    score = 0
    
    #set initial choices
    game_choices["A"] = random_entry(game_data.data)
    game_choices["B"] = random_entry(game_data.data)
    print(art.logo)
    
    while running:
        
        
        print_entry(game_choices["A"])
        print(art.vs)
        print_entry(game_choices["B"])

        response = input("Who has more followers? Type 'A' or 'B' ").upper()

        if response == compare_follower_counts(game_choices["A"],game_choices["B"]):
            score += 1
            os.system("clear")
            print(art.logo)
            print(f"You are right! Current Score is {score}")
            game_choices["A"] = game_choices[response]
            game_choices["B"] = random_entry(game_data.data)
        else:
            print(f"You are wrong. Final Score is {score}")
            running = False

game()