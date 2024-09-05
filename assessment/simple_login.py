# Nicholas Piet - 2024
# TAFE - Unit ICTPRG302 - Task 2
# Login Script
from os import system, name
from string import punctuation
from time import sleep
import re


# Clears the terminal
def clear_screen(): 
    system('cls' if name == 'nt' else 'clear')


clear_screen()

ESCAPED_SYMBOLS = re.escape(punctuation)

PATTERN_CHARS = re.compile(r'[A-Z]')
PATTERN_NUM = re.compile(r'\d')
PATTERN_SYM = re.compile(fr'[{ESCAPED_SYMBOLS}]')


def create_account():
    username_choice = input("Enter the username you would like to use: ")
    with open("accounts.txt", 'a+', encoding="utf-8") as accounts:
        accounts.seek(0)
        
        for user_accounts in accounts:
            username, _ = user_accounts.strip().split(",")
            if username_choice == username:
                print("Sorry, username not available. Please try again.\n")
                sleep(2)
                return
            
        print("Username available!\n")
        print("Please enter a password. "
              "Password requirements: 8 characters minimum, at least one symbol, number and uppercase letter.")
        
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
        accounts.write(f"{username_choice},{registration_password}\n")


def user_login():
    user_option = input("Enter your username: ").lower()
    print("Searching...")
    with open("accounts.txt", "r", encoding="utf-8") as user_accounts:
        for accounts in user_accounts:
            user, password = accounts.strip().split(",")
            if user == user_option:
                print("Username found.")
                user_password = input(f"Hello {user_option}, please enter your password: ")
                if user_password == password:
                    print("Login successful.\nOptions: (v)iew accounts, (e)xit.")
                    user_option = input("Enter an option: ")

                    if user_option in ("v", "view"):
                        view_accounts()
                        return
                    elif user_option in ("e", "exit"):
                        return
                    else:
                        print(f"Invalid option: '{option}'")

                elif password != user_password:
                    print("Incorrect password.")
                    
                    count = 0
                    while count < 3:
                        user_password = input(f"Password: ")
                        count += 1

                        if user_password == password:
                            user_option = input("Login successful")

                        elif count == 3:
                            sleep(2)
                            print("Sorry, please try again.\n")
                            return
        print(f"Error: User {user_option} not found.")


def view_accounts():
    with open("assets/accounts.txt", 'r', encoding="utf-8") as user_accounts:
        for accounts in user_accounts:
            user, password = accounts.strip().split(",")
            print(user)
        print("\nDone.")
        #   add: add number of accounts found.


def user_help():
    with open("assets/help.txt", "r", encoding="utf-8") as helpfile:
        for lines in helpfile:
            print(lines.strip())
        print()


option = ""
while option != "e":
    print("Login program\n"
          "(c)reate user account, (l)ogin, (h)elp and (e)xit")
    option = input("Please select an option: ").lower()

    if option in ("c", "create"):
        create_account()

    elif option in ("l", "login"):
        user_login()

    elif option in ("v", "view"):
        print("You need to be logged in to view accounts.\n")

    elif option in ("h", "help", "?"):
        user_help()
    
    elif option in ("e", "exit"):
        print("Exiting...")
        sleep(2)
        exit()
    
    else:
        print(f"Invalid option: '{option}'")
        print("Type 'help' for more information.\n")
        sleep(1)
        clear_screen()
