# Nicholas Piet - 2024
# TAFE - Unit ICTPRG302 - Task 2
# Login Script

from os import system, name
from string import punctuation
from time import sleep, time
from re import compile, escape
from passwd_module import password_gen

ESCAPED_SYMBOLS = escape(punctuation)
PATTERN_CHARS = compile(r'[A-Z]')
PATTERN_NUM = compile(r'\d')
PATTERN_SYM = compile(fr'[{ESCAPED_SYMBOLS}]')
MAX_ATTEMPTS = 4


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def password_creation():
    while True:
        password_choice = input("Enter a password: ").strip()
        
        if len(password_choice) < 8:
            print("Your password must be longer than 8 characters. Please try again.\n")
        elif not PATTERN_CHARS.search(password_choice):
            print("Your password does not contain any uppercase characters. Please try again.\n")
        elif not PATTERN_NUM.search(password_choice):
            print("Your password does not contain any numbers. Please try again.\n")  
        else:
            print("Password meets all requirements.")
            return password_choice


def login_submenu():
    print("Options: (v)iew accounts, (e)xit")
    submenu_option = input("Enter an option: ").lower().strip()
    
    if submenu_option in ("v", "view"):
        view_accounts()
        return login_submenu()
    elif submenu_option in ("e", "exit"):
        print("Exiting to main menu...")
        sleep(2)
        clear_screen()
        return main_menu() 
    else:
        print(f"Invalid option: '{submenu_option}'\n")
        return login_submenu()
    

def create_account():
    username_choice = input("Enter the username you would like to use: ").lower().replace(" ", "_")
    with open("assets/accounts.txt", 'a+', encoding="utf-8") as accounts:
        accounts.seek(0)
        for user_accounts in accounts:
            username, _ = user_accounts.strip().split(",")
            
            if username_choice == username:
                print(f"Sorry, the username '{username_choice}' is not available. Please try again.\n")
                sleep(2)
                clear_screen()
                return            
            elif username_choice == "":
                print(f"Sorry, blank entries are not allowed. Please try again.\n")
                sleep(2)
                clear_screen()
                return
            
        print(f"Username '{username_choice}' is available.")
        print("Please enter a password.\n")
        submenu_option = input("Please choose an option:\n"
                                "(g)enerate a new password (automatically) or,\n"
                                "(c)reate a password\n"
                                "Type 'cancel' to return to the main menu: ").lower().strip()

        if submenu_option in ("create", "c"):
            print("Password requirements: 8 characters minimum and "
                  "at least one number and uppercase letter.")
            registration_password = password_creation()       
        elif submenu_option in ("gen", "generate", "g"):
            registration_password = password_gen()  
        elif submenu_option in ("cancel", "exit"):
            clear_screen()
            return          
        else:
            print(f"Invalid option: '{submenu_option}'\n")
            return create_account()

        print("Writing...")
        print("Account creation successful.\n")
        print(f"Username: {username_choice}\nPassword: {registration_password}\n")
        accounts.write(f"{username_choice},{registration_password}\n")


def user_login():
    user_option = input("Enter your username: ").lower().replace(" ", "_")
    print("Searching...")
    with open("assets/accounts.txt", "r", encoding="utf-8") as user_accounts:
        for accounts in user_accounts:
            username, password = accounts.strip().split(",")
            
            if username == user_option:
                print("Success! Account exists.")
                user_password = input(f"Please enter your password: ").strip()
                if password == user_password:
                    print(f"\nYou are logged in as: {username}.")
                    login_submenu()        
                
                elif password != user_password:    
                    count = 0
                    while count < 3:
                        count += 1
                        user_password = input(f"Incorrect password. "
                                              f"You have {MAX_ATTEMPTS - count} attempt(s) remaining: ")
                        
                        if user_password == password:
                            print(f"\nYou are logged in as: {username}.")
                            login_submenu()
                        elif count == 3:
                            print("Sorry, please try again.\n")
                            sleep(2)
                            clear_screen()
                            return
                        
        print(f"Error: User '{user_option}' not found.\n")
        sleep(2)
        clear_screen()
        return


def view_accounts():
    count = 0
    start_time = time()
    with open("assets/accounts.txt", 'r', encoding="utf-8") as user_accounts:
        for accounts in user_accounts:
            count += 1
            username, _ = accounts.strip().split(",")
            print(username)
        end_time = time()
        exec_time = end_time - start_time
        print(f"\nQuery complete: {count} accounts found.")
        print(f"Execution took {exec_time:.3f}s\n")


def user_help():
    with open("assets/help.txt", "r", encoding="utf-8") as helpfile:
        for lines in helpfile:
            print(lines.strip())
        print()


def main_menu():
    option = ""
    while option != "e":
        print("Gelos Simple Login\n")
        print("Options: (c)reate account, (l)ogin and (e)xit.\n"
              "To view accounts, please log in.\n")
        option = input("Please select an option: ").lower().strip()

        if option in ("c", "create"):
            create_account()
        elif option in ("l", "login"):
            user_login()
        elif option in ("v", "view"):
            print("Error: You need to be logged in to view accounts.\n")
            sleep(2)
            clear_screen()
        elif option in ("h", "help", "?"):
            user_help()
        elif option in ("e", "exit"):
            print("Exiting...")
            sleep(2)
            clear_screen()
            exit()
        else:
            print(f"Invalid option: '{option}'")
            print("Type 'help' for more information.\n")
            sleep(2)
            clear_screen()

clear_screen()
main_menu()
