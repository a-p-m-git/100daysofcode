alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    encoded = ""
    
    for letter in text:
        print(f"{alphabet.index(letter)} / {shift} / {alphabet.index(letter) + shift} / {len(alphabet)}")
        if (alphabet.index(letter) + shift) >= len(alphabet):
            newShift = (shift - (len(alphabet) - alphabet.index(letter)))
            print(f"{letter} shifted {shift} - {newShift} will put it outside bounds of alphabet index")
            encoded += alphabet[newShift]
        else:
            print(f"{alphabet[alphabet.index(letter)]} -> {alphabet[alphabet.index(letter) + shift]}")
            encoded += alphabet[alphabet.index(letter) + shift]

    print(f"The encode text is {encoded}")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text,shift)