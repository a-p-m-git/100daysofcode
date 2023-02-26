import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
running = True

def caesar(text, shift, action):
    encoded = ""

    if action == "encode":
        for letter in text:
            #print(f"{alphabet.index(letter)} / {shift} / {alphabet.index(letter) - shift} / {len(alphabet)}")
            if not (alphabet.count(letter)):
                print(letter)
                encoded += letter
            elif (alphabet.index(letter) + shift) >= len(alphabet):
                newShift = alphabet.index(letter) - shift
                #print(f"{letter} shifted {shift} - {newShift} {alphabet.index(letter) - shift} will put it outside bounds of alphabet index")
                #print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[newShift]}")
                encoded += alphabet[newShift]
            else:
                #print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[alphabet.index(letter) + shift]}")
                encoded += alphabet[alphabet.index(letter) + shift]
    elif action == "decode":
        for letter in text:
            #print(f"{alphabet.index(letter)} / {shift} / {alphabet.index(letter) - shift} / {len(alphabet)}")
            if not (alphabet.count(letter)):
                print(letter)
                encoded += letter
            elif (alphabet.index(letter) - shift) <= 0:
                newShift = alphabet.index(letter) - shift
             #   print(f"{letter} shifted {shift} - {newShift} will put it outside bounds of alphabet index")
             #   print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[alphabet.index(letter) + shift]}")
                encoded += alphabet[newShift]
            else:
                #print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[alphabet.index(letter) - shift]}")
                encoded += alphabet[alphabet.index(letter) - shift]

    print(f"The encode text is {encoded}")

while running:
    print(art.logo)
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    
    shift = int(input("Type the shift number:\n"))

    while shift < 0 or shift > 26:
        print(f"{shift} value is invalid. Please choose a number between 1 and 26")
        shift = int(input("Type the shift number: "))

    caesar(text,shift,direction)
    if input("Do you want to try again? [Y\\n]").lower() == 'n':
        running=False

#day8 complete!