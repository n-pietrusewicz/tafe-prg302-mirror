# ask user for username
# read accounts file
    # if account exists in the file, display an error
# end up here if the account is available
# prompt for password OR generate a password and display it.

print("Registration function")
with open("accounts.txt", 'r') as accounts:
    for lines in accounts:
        username, password = accounts.split(",").strip()
        print(username)