import random

numbers = "0123456789"
letters = "abcdefghijklmnoqprstuvwyzxABCDEFGHIJKLMNOQPRSTUYWVZX"
symbols = "!@#$^&*?"
tempPassword = []
password = ""

print("Welcome to the PyPassword Generator!\n")

letterCount = int(input("How many letters would you like your password to be?\n"))
symbolCount = int(input("How many special symbols?\n"))
numberCount = int(input("How many numbers?\n"))

totalCount = int(letterCount) + int(symbolCount) + int(numberCount)
#print(totalCount)

for n in range(0,letterCount):
    tempPassword.append(letters[random.randint(0,len(letters) - 1)])

for n in range(0,symbolCount):
    tempPassword.append(symbols[random.randint(0,len(symbols) - 1)])

for n in range(0,numberCount):
    tempPassword.append(numbers[random.randint(0,len(numbers) - 1)])

random.shuffle(tempPassword)
print("".join(tempPassword))
