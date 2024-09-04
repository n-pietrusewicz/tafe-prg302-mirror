# Nicholas Piet - 2024
# TAFE - Unit ICTPRG302 - Task 2
# Login Script
from string import punctuation
from time import sleep
import re

escaped_symbols = re.escape(punctuation)

PATTERN_CHARS = re.compile(r'[A-Z]')
PATTERN_NUM = re.compile(r'\d')
PATTERN_SYM = re.compile(fr'[{escaped_symbols}]')

def create_account():
    username_choice = input("Enter the username you would like to use: ")
    with open("accounts.txt", 'a+') as accounts:
        accounts.seek(0)
        
        for user_accounts in accounts:
            username, _ = user_accounts.strip().split(",")
            if username_choice == username:
                print("Sorry, username not available. Please try again.\n")
                sleep(2)
                return
            
        print("Username available!\n")
        print("Please enter a password."
              "Password requirements: 8 characters minimum, at least one symbol, number and uppercase letter.")
        password_choice = input("Password: ")
        if len(password_choice) < 8:
            print("Your password must be longer than 8 characters. Please try again.\n")
        elif not PATTERN_CHARS.search(password_choice):
            print("Your password does not contain any uppercase characters. Please try again.")
        # elif not Pattern(PATTERN_NUM):
        #     print("Your password does not contain any numbers. Please try again.")
        elif not PATTERN_SYM.search(password_choice):
            print("Your password does not contain any special characters. Please try again.")

        else:
            print("Password is OK")
            return
        
        


def user_login():
    print("Login\n")


def view_accounts():
    print("View accounts\n")


def user_help():
    print("Help\n")


option = ""
while option != "e":
    print("Login program\n"
          "(c)reate user account, (l)ogin, (v)iew accounts, (h)elp and (e)xit")
    option = input("Please select an option: ").lower()

    if option == "c":
        create_account()

    elif option == "l":
        user_login()

    elif option == "v":
        view_accounts()
    
    elif option in ("h", "help", "?"):
        user_help()
    
    elif option == "e":
        print("Exiting...")
    
    else:
        print(f"Invalid option: '{option}'")
        print("Type 'help' for more information.\n")
