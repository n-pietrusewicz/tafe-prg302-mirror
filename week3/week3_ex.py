def create_contact():
    print("Creating a contact...")
    contact_file = open("contacts.txt", 'a')
    new_contact_name = input("Enter the new contact's full name: ")
    new_contact_phone = input("Enter the new contact's phone number: ")
    new_contact_email = input("Enter the new contact's email: ")
    contact_file.write(f"{new_contact_name}\t{new_contact_phone}"
                       f"\t{new_contact_email}\n")
    print("Contact has been added with the following information:\n"
          f"{new_contact_name}\n{new_contact_phone}\n{new_contact_email}")
    contact_file.close()


def search_contacts():
    print("\nSearch contacts function\n")
    # find_string = input("Enter a string to search\n"
    #                     "(name, phone or email): ")
    # contact_file = open("contacts.txt", "r").readlines(find_string)


def view_contacts():
    print("\nOpening contacts.txt...\n")
    contact_file = open("contacts.txt", 'r')
    for contact in contact_file:
        print(contact.strip())


menuChoice = "*"
while menuChoice != "e":
    print("==========================\n"
          "= Nick's Contact Program =\n"
          "==========================\n")

    # print("1) Create contact.")
    # print("2) Search contacts.")
    # print("3) View all contacts.")
    # print("4) Exit.")

    menuChoice = input("Enter an option:\n"
                       "(c)reate contact, (s)earch, (v)iew or (e)xit: ")
    if menuChoice == "c":
        create_contact()
    elif menuChoice == "s":
        search_contacts()
    elif menuChoice == "v":
        view_contacts()
    elif menuChoice == "e":
        print("\nExiting...\n")
    else:
        print(f"{menuChoice} is an invalid option...\n")
