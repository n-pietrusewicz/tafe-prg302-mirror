# Nicholas Piet - 2024
# TAFE - Unit ICTPRG302 - Task 2
# Login Script

def create_account():
    print("Create account")


def user_login():
    print("Login")


def view_accounts():
    print("View accounts")


def user_help():
    print("Help")


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
