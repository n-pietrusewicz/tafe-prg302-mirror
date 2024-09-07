from secrets import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

ALPHANUMERIC = ascii_uppercase + ascii_lowercase
ALL_CHARS = ALPHANUMERIC + digits + punctuation
NO_SPECIAL_CHARS = ALPHANUMERIC + digits


def password_gen():
    while True:
        try: 
            user_choice = int(input("Enter a password length (8-512 characters): "))
            if 8 <= user_choice <= 512:
                
                option = input("Would you like special characters? (y)es/(n)o: ").lower().strip()
                if option in ("y", "yes"):
                    generated_password = ''.join(choice(ALL_CHARS) for _ in range(user_choice))
                    return generated_password
            
                elif option in ("n", "no"):
                    generated_password = ''.join(choice(NO_SPECIAL_CHARS) for _ in range(user_choice))
                    return generated_password
            else:
                print("Sorry! Length must be between 8 and 512.")
        except ValueError:
            print("Error: Invalid value")
