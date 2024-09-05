# password module
# generates a random password with error handling capabilties.

import secrets
import string
CHARS = string.ascii_letters + string.digits + string.punctuation

def password_gen():
    try: 
        user_choice = int(input("Enter a password length choice (8-512 characters): "))
        if 8 <= user_choice <= 512:
            password = ''.join(secrets.choice(CHARS) for i in range(user_choice))
            print(password)
        else:
            print("Sorry! Length must be between 8 and 512.")
    except ValueError:
        print("Error: Invalid value")


