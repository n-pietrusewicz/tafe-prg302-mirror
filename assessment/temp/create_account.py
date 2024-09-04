# ask user for username
# read accounts file
    # if account exists in the file, display an error
# end up here if the account is available
# prompt for password OR generate a password and display it.

print("Registration function")
user_choice = input("Enter the username you would like to use: ")
with open("accounts.txt", 'a+') as accounts:
    accounts.seek(0)
    for user_accounts in accounts:
        username, passwords = user_accounts.strip().split(",")
        if user_choice == username:
            print("Sorry, username not available. Please try again.")
            exit()
    print("Username available!")
    