from caesar_cipher_art import caesar_cipher_logo

print("Day 8 - 100 Days of Code.")
print("Welcome to Caesar Cipher.")
print(caesar_cipher_logo)

empty_string = ""
does_user_wish_to_continue = True


def encode_decode_message(user_input = empty_string, shift = 0):
    """
    Description:
        Method to encode and decode messages based on a set shift value.
    Returns:
        str: Encoded/Decoded message.
    """
    return empty_string.join([chr(ord(element) + shift) for element in user_input])


while does_user_wish_to_continue:
    user_entry = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    secret_message = input("Enter the message:\n")
    shift_value = int(input("Enter the shift value:\n"))
    if user_entry == "encode":
        print(f"Here is your encoded message {encode_decode_message(user_entry, shift_value)}")
    elif user_entry == "decode":
        shift_value *= -1
        print(f"Here is your decoded message {encode_decode_message(user_entry, shift_value)}")
    does_user_wish_to_continue = True if input("Do you wish to continue (yes/no)?\n").lower() == "yes" else False
    if not does_user_wish_to_continue:
        print("Goodbye!")
