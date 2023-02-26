alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encoded = ""
    
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

    print(f"The encode text is {encoded}")

def decrypt(text, shift):
    deCoded = ""
    
    for letter in text:
        print(f"{alphabet.index(letter)} / {shift} / {alphabet.index(letter) - shift} / {len(alphabet)}")
        if (alphabet.index(letter) - shift) <= 0:
            newShift = alphabet.index(letter) - shift
            print(f"{letter} shifted {shift} - {newShift} will put it outside bounds of alphabet index")
            print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[alphabet.index(letter) + shift]}")
            deCoded += alphabet[newShift]
        else:
            print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[alphabet.index(letter) - shift]}")
            deCoded += alphabet[alphabet.index(letter) - shift]

    print(f"The decoded text is {deCoded}")
    



#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == "encode":
    encrypt(text,shift)
else:
    decrypt(text,shift)