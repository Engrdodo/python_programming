import string

lower = string.ascii_lowercase
alphabet = list(lower + lower)


def caesar(start_text,  shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode": #checks decode first to reduce code
        shift_amount *= -1
    for char in start_text:
        if char in  alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char #appends number, space and other character
    print(f"The {cipher_direction}d text is [{end_text}] ")

print("Welcome! You can send your highly sensitive messages with our CAESAR THE CIPHER Program ")
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25   #captures if a user enters a really large shift_amount
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_end = True
        print("Goodbye")



    
