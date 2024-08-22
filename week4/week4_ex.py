def create_contact():
    print("Creating a contact...")
    contact_file = open("contacts-week4.txt", 'a')
    new_contact_name = input("\nEnter the new contact's full name: ").title()
    new_contact_phone = input("Enter the new contact's phone number: ")
    new_contact_email = input("Enter the new contact's email: ").lower()
    contact_file.write(f"{new_contact_name}\t{new_contact_phone}"
                       f"\t{new_contact_email}\n")
    print("Contact has been added with the following information:\n"
          f"{new_contact_name}\n{new_contact_phone}\n{new_contact_email}")
    contact_file.close()


def search_by_name():
    print("\nSearching by name")
    search_val = input("Q: ").title()

    with open('contacts-week4.txt', 'r') as contacts_file:
        contact_found = False
        for contacts in contacts_file:
            name, phone, email = contacts.split("\t")
            if name == search_val:
                print(f"A: {name} {phone} {email}".strip())
                contact_found = True
        if not contact_found:
            print(f"E: {search_val} not found. Is the contact in the list?")


def search_by_phone():
    print("\nSearch by phone")
    search_val = str(input("Q: "))

    with open('contacts-week4.txt', 'r') as contacts_file:
        contact_found = False
        for contacts in contacts_file:
            name, phone, email = contacts.split("\t")
            if phone.replace(" ", "").replace("-","") == \
                search_val.replace(" ", "").replace("-", ""):
                print(f"A: {name} {phone} {email}".strip())
                contact_found = True
        if not contact_found:
            print(f"E: {search_val} not found. Is the contact in the list?")


def search_by_email():
    print("\nSearching by email")
    search_val = input("Q: ").lower()
    with open('contacts-week4.txt', 'r') as contacts_file:
        contact_found = False
        for contacts in contacts_file:
            name, phone, email = contacts.split("\t")
            if email.strip() == search_val:
                print(f"A: {name} {phone} {email}".strip())
                contact_found = True
        if not contact_found:
            print(f"E: '{search_val}' not found. Is this contact in the list?")


def search_contacts():
    print("\nSearch contacts function\n")
    print("Search by (n)ame, search by (p)hone or by (e)mail address")
    print("'b' to head back to the main menu")
    search_mode = input("Enter your choice: ").lower()
    if search_mode == "n":
        search_by_name()
    elif search_mode == "p":
        search_by_phone()
    elif search_mode == "e":
        search_by_email()
    elif search_mode == "b":
        print()
        return
    else:
        print(f"\nInvalid option '{search_mode}'.")


def view_contacts():
    print("\nOpening contacts.txt...\n")
    with open("contacts-week4.txt", 'r') as contact_file:
        print("View contacts")
        for contacts in contact_file:
            name, phone, email = contacts.split("\t")
            print(name, phone, email.strip())
        print()


menuChoice = ""
while menuChoice != "e":
    print("==========================\n"
          "= Nick's Contact Program =\n"
          "==========================\n")

    menuChoice = input("Enter an option:\n"
                       "(c)reate contact, (s)earch, (v)iew or (e)xit: ").lower()
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
