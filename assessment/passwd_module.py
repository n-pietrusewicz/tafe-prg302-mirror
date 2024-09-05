from secrets import choice
from string import ascii_letters, digits, punctuation

ALL_CHARS = ascii_letters + digits + punctuation
NO_SPECIAL_CHARS = ascii_letters + digits


def password_gen():
    try: 
        user_choice = int(input("Enter a password length choice (8-512 characters): "))
        if 8 <= user_choice <= 512:
            
            option = input("Would you like special characters? ").lower()
            if option in ("y", "yes"):
                generated_password = ''.join(choice(ALL_CHARS) for i in range(user_choice))
                print(generated_password)
                return generated_password
            elif option in ("n", "no"):
                generated_password = ''.join(choice(NO_SPECIAL_CHARS) for i in range(user_choice))
                print(generated_password)
                return generated_password
        else:
            print("Sorry! Length must be between 8 and 512.")
    except ValueError:
        print("Error: Invalid value")
