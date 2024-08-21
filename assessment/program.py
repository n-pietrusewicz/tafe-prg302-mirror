def create_account():
    print("Create account function")
    user_option = input(r"Enter the username you would like to use: ").lower()
    with open("assets/accounts.txt", "a+") as user_accounts:
        user_accounts.seek(0)
        for accounts in user_accounts:
            user, password = accounts.strip().split(",")

            if user == user_option:
                print(f"Username {user_option} taken. Please try again.")
                return
            
            # if user != user_option:
        print(f"Username {user_option} available.")
        user_password = input("Enter a password: ")
        print("Writing...")
        user_accounts.write(f"{user_option},{user_password}\n")

                
                 
    

def user_login():
    print("Login function\n")
    user_option = input("Enter your username.\nType 'c' to cancel: ").lower()
    with open("assets/accounts.txt", "r") as user_accounts:
        # user_accounts.seek(0)
        for accounts in user_accounts:
            user, password = accounts.strip().split(",")

            if user != user_option:
                print("Incorrect username.\n")
                return
            
            elif user == user_option:
                print("Username OK")
                user_password = input(f"Hello, {user_option} please enter your password: ")
                
                
                if password != user_password:
                    print("Incorrect password.")
                    count = 0
                   
                    while count < 3:
                        user_password = input(f"Password: ")
                        count = count + 1

                        if count == 3:
                            print("Authentication failed. Please login and try again.")
                            return
                        
                elif password == user_password:
                    print("Login success.")
                    user_option = input("(e)xit or (m)enu.\n?: ").lower()

                    if user_option in ('m', 'menu'):
                        print("Exiting...\n ")
                        return
                    
                    elif user_option in ('e', 'exit'):
                        exit()
                    
                    else:
                        print(f"Invalid option: {user_option}\n")



def view_accounts():
    with open("assets/accounts.txt", 'r') as user_accounts:
        for accounts in user_accounts:
            user, password = accounts.strip().split(",")
            print(user)


def user_help():
    with open("assets/help.txt", 'r') as help_file:
        for lines in help_file:
            lines = lines.strip()
            print(lines)


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