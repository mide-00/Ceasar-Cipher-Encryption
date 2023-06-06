#!/usr/bin/env python

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Combined the encrypt() and decrypt() functions below into a single function called caesar().
# Also added a new variable called

def caesar(input_text, shift_amount, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        final_text += alphabet[new_position]

    # using an f string to allow "direction" variable to be used dynamically in the final print statement
    print(f"Here's the {direction}d result: {final_text}")


caesar(input_text=text, shift_amount=shift, cipher_direction=direction)


# Encrypt function to encode text based on user direction input. This function shifts each letter of the 'text'
# *forward* in the alphabet by the shift amount and prints the encrypted text. e.g. input_text = "hello",
# shift = 5, encoded_text = #"mjqqt" . Function prints out: "The encoded text is mjqqt"

# def encrpyt(input_text, shift_amount):
#     encoded_text = ""
#     for letter in input_text:
#         letter_position = alphabet.index(letter)
#         new_letter_position = letter_position + shift_amount
#         new_letter = alphabet[new_letter_position]
#         encoded_text += new_letter
#     print(f"The encoded text is {encoded_text}")


# Decrypt function to decode text based on user direction input. This function shifts each letter of the 'text'
# *backwards* in the alphabet by the shift amount and prints the decrypted text. e.g. encoded_text = "mjqqt",
# shift = 5, input_text = "hello" . Function prints out: "The decoded text is hello"

# def decrypt(input_text, shift_amount):
#     decoded_text = ""
#     for letter in input_text:
#         letter_position = alphabet.index(letter)
#         new_letter_position = letter_position - shift_amount
#         new_letter = alphabet[new_letter_position]
#         decoded_text += new_letter
#     print(f"The decoded text is {decoded_text}")
#
#
# if direction == "encode":
#     encrpyt(input_text=text, shift_amount=shift)
# elif direction:
#     decrypt(input_text=text, shift_amount=shift)
