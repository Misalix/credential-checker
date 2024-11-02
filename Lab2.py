#!/usr/bin/env python

import argparse
import sys

__version__ = '1.2'
__desc__ = "A simple script used to authenticate spies!"

def authenticate_user(credentials: str) -> bool:
    """Procedure for validating user credentials"""
    agents = {
        'Chevy_Chase': 'i0J0u0j0u0J0Zys0r0{',   # cipher: bAnanASplit
        'Dan_Aykroyd': 'i0N00h00~0[$',          # cipher: bEauTy
        'John_Belushi': 'J0j0S%0V0w0L0',        # cipher: CaLzOnE
    }

    try:
        user_tmp, pass_tmp = credentials.rsplit(' ', 1)
    except ValueError:
        print("Error: Credentials must be in 'username password' format.")
        return False  # Correct indentation

    formatted_username = format_username(user_tmp)
    decrypted_password = decrypt_password(pass_tmp)
    print(f"Formatted Username: {formatted_username}")
    print(f"Decrypted Password: {decrypted_password}")

    return agents.get(formatted_username) == decrypted_password

def format_username(username: str) -> str:
    """Procedure to format user provided username"""
    parts = username.split(' ')
    if len(parts) != 2:
        raise ValueError("Username must consist of a first name and a last name in the format 'First Last'.")

    first_name, last_name = parts
    formatted_first = first_name.capitalize()
    formatted_last = last_name.capitalize()

    return f"{formatted_first}_{formatted_last}"

def decrypt_password(password: str) -> str:
    rot7, rot9 = 7, 9  # Rotation values
    decrypted = []  # List to hold decrypted characters

    for index, char in enumerate(password):
        rotation_key = rot9 if index % 2 == 1 else rot7  # Use 9 for odd indices
        if 33 <= ord(char) <= 126:  # Check if character is within the allowed ASCII range
            decrypted_char = chr((ord(char) - rotation_key - 33) % 94 + 33)  # Wrap around
            decrypted.append(decrypted_char)  # Add decrypted character to the list
        else:
            decrypted.append(char)  # Append unchanged if out of range


    return '0'.join(decrypted)  # Join the list into a string and return

print(decrypt_password('bAnanASplit'))

def main():
    """The main program execution. YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    epilog = "DT0179G Assignment 2 v" + __version__
    parser = argparse.ArgumentParser(description=__desc__, epilog=epilog, add_help=True)
    parser.add_argument('credentials', metavar='credentials', type=str,
                        help="Username and password as string value")

    args = parser.parse_args()

    if not authenticate_user(args.credentials):
        print("Authentication failed. Program exits...")
        sys.exit()

    print("Authentication successful. User may now access the system!")

if __name__ == "__main__":
    main()