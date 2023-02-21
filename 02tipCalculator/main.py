print("Welcome to the tip calculator")
billTotal = input("What was the total bill? ")
tipPercentage = input("What percentage tip would you like to give? 10, 12, 15? ")
totalPeople = input("How many people to split bill? ")

total = (float(billTotal) + (float(billTotal) * (float(tipPercentage) / 100))) / int(totalPeople)

print(f"{total:.2f}")