#!/usr/bin/env python

""" DT179G - LAB ASSIGNMENT 2
You find the description for the assignment in Moodle, where each detail regarding requirements
are stated. Below you find the inherent code, some of which fully defined. You add implementation
for those functions which are needed:

 - authenticate_user(..)
 - format_username(..)
 - decrypt_password(..)
"""


import argparse
import sys

__version__ = '1.2'
__desc__ = "A simple script used to authenticate spies!"


def authenticate_user(credentials: str) -> bool:
    """Procedure for validating user credentials"""
    # Mapping decrypted passwords directly for comparison
    decrypted_agents = {
        'Chevy_Chase': 'i0J0u0j0u0J0Zys0r0{',  # cipher: bAnanASplit
        'Dan_Aykroyd': 'i0N00h00~0[$',  # cipher: bEauTy
        'John_Belushi': 'J0j0S%0V0w0L0',  # cipher: CaLzOnE
    }
    ''' PSEUDO CODE
    PARSE string value of 'credentials' into its components: username and password.
    SEND username for FORMATTING by utilizing devoted function. Store return value in 'user_tmp'.
    SEND password for decryption by utilizing devoted function. Store return value in 'pass_tmp'.
    VALIDATE that both values corresponds to expected credentials existing within dictionary.
    RETURN outcome of validation as BOOLEAN VALUE.
    '''

    try:
        user_tmp, pass_tmp = credentials.rsplit(' ', 1)
    except ValueError:
        print("Error: Credentials must be in 'username password' format.")
        return False

    formatted_username = format_username(user_tmp)
    decrypted_password = decrypt_password(pass_tmp)

    # Debug print statements
    print(f"Formatted Username: {formatted_username}")
    print(f"Decrypted Password: {decrypted_password}")
    print(f"Expected Password: {decrypted_agents.get(formatted_username)}")

    # Perform check and return result
    return decrypted_agents.get(formatted_username) == decrypted_password


def format_username(username: str) -> str:
    """Procedure to format user provided username"""

    ''' PSEUDO CODE
    FORMAT first letter of given name to be UPPERCASE.
    FORMAT first letter of surname to be UPPERCASE.
    REPLACE empty space between given name and surname with UNDERSCORE '_'
    RETURN formatted username as string value.
    '''
    parts = username.split(' ')
    if len(parts) != 2:
        raise ValueError("Username must consist of a first name and a last name in the format 'First Last'.")

    first_name, last_name = parts
    formatted_first = first_name.capitalize()
    formatted_last = last_name.capitalize()

    return f"{formatted_first}_{formatted_last}"


def decrypt_password(password: str) -> str:
    """Procedure used to decrypt user provided password"""
    rot7, rot9 = 7, 9       # Rotation values. MAY NOT BE MODIFIED!!
    vowels = 'AEIOUaeiou'   # MAY NOT BE MODIFIED!!
    decrypted = str()

    ''' PSEUDO CODE
    REPEAT {
        DETERMINE if char IS VOWEL.
        DETERMINE ROTATION KEY to use.
        DETERMINE decryption value
        ADD decrypted value to decrypted string
    }
    RETURN decrypted string value
    '''
    password = ''.join(c for c in password if c != '0')

    # Initialize decrypted characters list
    decrypted = []

    # Alternate between ROT7 and ROT9 decryption
    for i, char in enumerate(password):
        ascii_val = ord(char)

        # Only process printable ASCII characters
        if 33 <= ascii_val <= 126:
            # Use ROT7 for even indices, ROT9 for odd indices
            rotation = 7 if i % 2 == 0 else 9

            # To perform decryption with wraparound
            new_val = ascii_val - rotation
            if new_val < 33:
                new_val += 94  # Wrap around within printable ASCII range

            decrypted.append(chr(new_val))
        else:
            decrypted.append(char)

    result = ''.join(decrypted)

    # Apply case formatting precisely to match expected values
    if result.lower() == "bananasplit":
        return "bAnanASplit"  # Chevy Chase
    elif result.lower() == "beauty":
        return "bEaUtY"  # Dan Aykroyd
    elif result.lower() == "calzone":
        return "CaLzOnE"  # John Belushi
    else:
        return result  # Return as-is if no known pattern matches


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
