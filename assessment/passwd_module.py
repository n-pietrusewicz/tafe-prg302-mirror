from random import shuffle
from secrets import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

ALPHANUMERIC = ascii_uppercase + ascii_lowercase
ALL_CHARS = ALPHANUMERIC + digits + punctuation
NO_SPECIAL_CHARS = ALPHANUMERIC + digits


def password_gen():
    while True:
        try:
            user_choice = int(input("Enter a password length (10-512 characters): "))
            if 10 <= user_choice <= 512:
                option = input("Would you like special characters? (y)es/(n)o: ").lower().strip()
                if option in ("y", "yes"):
                    generated_password = [choice(ascii_uppercase)]
                    generated_password += [choice(ALL_CHARS) for _ in range(user_choice - 1)]
                elif option in ("n", "no"):
                    generated_password = [choice(ascii_uppercase)]
                    generated_password += [choice(NO_SPECIAL_CHARS) for _ in range(user_choice - 1)]
                shuffle(generated_password)
                generated_password = ''.join(generated_password)
                return generated_password
            print("Sorry! Length must be between 10 and 512.")
        except ValueError:
            print("Error: Invalid value")
