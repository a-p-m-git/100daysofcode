alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text, shift, action):
    encoded = ""
    
    if action == "encode":
        for letter in text:
            print(f"{alphabet.index(letter)} / {shift} / {alphabet.index(letter) - shift} / {len(alphabet)}")
            if (alphabet.index(letter) + shift) >= len(alphabet):
                newShift = alphabet.index(letter) - shift
                print(f"{letter} shifted {shift} - {newShift} {alphabet.index(letter) - shift} will put it outside bounds of alphabet index")
                print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[newShift]}")
                encoded += alphabet[newShift]
            else:
                print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[alphabet.index(letter) + shift]}")
                encoded += alphabet[alphabet.index(letter) + shift]
    elif action == "decode":
        for letter in text:
            print(f"{alphabet.index(letter)} / {shift} / {alphabet.index(letter) - shift} / {len(alphabet)}")
            if (alphabet.index(letter) - shift) <= 0:
                newShift = alphabet.index(letter) - shift
                print(f"{letter} shifted {shift} - {newShift} will put it outside bounds of alphabet index")
                print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[alphabet.index(letter) + shift]}")
                encoded += alphabet[newShift]
            else:
                print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[alphabet.index(letter) - shift]}")
                encoded += alphabet[alphabet.index(letter) - shift]

    print(f"The encode text is {encoded}")

    

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text,shift,direction)