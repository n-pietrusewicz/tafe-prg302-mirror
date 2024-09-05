# Nicholas Piet - 2024
# TAFE - Unit ICTPRG302 - Task 2
# Login Script

from os import system, name
from string import punctuation
from time import sleep
import re

# Declare constant for punctuation symbols and use escape characters for any conflicting symbols
ESCAPED_SYMBOLS = re.escape(punctuation)

# Declaring constants for password string validation and compile regex search operators.
PATTERN_CHARS = re.compile(r'[A-Z]')
PATTERN_NUM = re.compile(r'\d')
PATTERN_SYM = re.compile(fr'[{ESCAPED_SYMBOLS}]')

# Clears the terminal
def clear_screen(): 
    system('cls' if name == 'nt' else 'clear')


def create_account():
    username_choice = input("Enter the username you would like to use: ")
    with open("assets/accounts.txt", 'a+', encoding="utf-8") as accounts:
        accounts.seek(0)
        
        for user_accounts in accounts:
            username, _ = user_accounts.strip().split(",")
            if username_choice == username:
                print("Sorry, username not available. Please try again.\n")
                sleep(2)
                return
            
        print(f"Username {username_choice} available\n")
        print("Please enter a password.\n")
        print("Password requirements: 8 characters minimum, at least one symbol, number and uppercase letter.")
        
        def password_validation():
            while True:
                password_choice = input("Password: ")
                if len(password_choice) < 8:
                    print("Your password must be longer than 8 characters. Please try again.\n")
                elif not PATTERN_CHARS.search(password_choice):
                    print("Your password does not contain any uppercase characters. Please try again.")
                elif not PATTERN_NUM.search(password_choice):
                    print("Your password does not contain any numbers. Please try again.")
                elif not PATTERN_SYM.search(password_choice):
                    print("Your password does not contain any special characters. Please try again.")
                
                else:
                    print("Password meets all requirements.")
                    return password_choice
                
        registration_password = password_validation()
        print("Writing...")
        print("Account creation successful.")
        print(f"Username: {username_choice}\nPassword: {registration_password}")
        accounts.write(f"{username_choice},{registration_password}\n")


def user_login():
    user_option = input("Enter your username: ").lower()
    print("Searching...")
    with open("assets/accounts.txt", "r", encoding="utf-8") as accounts:
        for accounts in accounts:
            user, password = accounts.strip().split(",")
            if user == user_option:
                print("Account found.")
                user_password = input(f"Hello {user}, please enter your password: ")

                def login_submenu():
                    print(f"You are logged in as: {user}.\nOptions: (v)iew accounts, (e)xit.")
                    user_option = input("Enter an option: ")

                    if user_option in ("v", "view"):
                            view_accounts()
                            print()
                            return login_submenu()
                    elif user_option in ("e", "exit"):
                            print()
                            return main_menu()
                    else:
                        print(f"Invalid option: '{user_option}'")
                if password == user_password:
                    login_submenu()
                if password != user_password:
                    print("Incorrect password. Please try again.")
                    
                    count = 0
                    count_state = 4
                    while count < 3:
                        count += 1
                        count_state -= 1
                        user_password = input(f"Incorrect password. You have {count_state} attempts remaining: ")


                        if user_password == password:
                            login_submenu()

                        elif count == 3:
                            sleep(2)
                            print("Sorry, please try again.\n")
                            return
                        
        if user != user_option:
            print(f"Error: User {user_option} not found.\n")
            sleep(2)
            clear_screen()
            return


def view_accounts():
    count = 0
    with open("assets/accounts.txt", 'r', encoding="utf-8") as accounts:
        for accounts in accounts:
            count += 1
            user, password = accounts.strip().split(",")
            print(user)
        print("\nDone.")
        print(f"Query complete: {count} accounts found.")
        return


def user_help():
    with open("assets/help.txt", "r", encoding="utf-8") as helpfile:
        for lines in helpfile:
            print(lines.strip())
        print()
        return


def main_menu():
    option = ""
    while option != "e":
        print("Gelos Simple Login\n")
        print("Options: (c)reate user account, (l)ogin, (h)elp and (e)xit. To view accounts, please log in.")
        option = input("Please select an option: ").lower()

        if option in ("c", "create"):
            create_account()

        elif option in ("l", "login"):
            user_login()

        elif option in ("v", "view"):
            print("Error: You need to be logged in to view accounts.\n")

        elif option in ("h", "help", "?"):
            user_help()
        
        elif option in ("e", "exit"):
            print("Exiting...")
            sleep(2)
            exit()
        
        else:
            print(f"Invalid option: '{option}'")
            print("Type 'help' for more information.\n")
            sleep(1.5)
            clear_screen()

clear_screen()
main_menu()
