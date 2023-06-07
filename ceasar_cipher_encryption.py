#!/usr/bin/env python

# Importing logo from art.py
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Creating a single function called ceasar() able to encode/decode.

def caesar(input_text, shift_amount, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    # Note: Changed "letter" variable to "character"
    for character in input_text:
        # Checking if Characters entered by user is in the list of characters provided
        if character in alphabet:
            position = alphabet.index(character)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        else:
            # Encoding/Decoding only the letters and adding other characters entered by the user as they are.
            final_text += character

    # using an f string to allow "cipher_direction" variable to be used dynamically in the final print statement
    print(f"Here's the {cipher_direction}d result: {final_text}")


# Printing the cipher logo imported for art.py to show at the start of the program
print(logo)

should_Continue = True
while should_Continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Catching a bug here incase user enters a shift that is greater than the number of letters in the alphabet.
    # For example running the program and entering a shift number of 45, the program continues to work even if the user
    # enters a shift number greater than 26.
    shift = shift % 26
    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_Continue = False
        print("Goodbye")

