import phonebook_module

contacts = {}  # Dictionary to store contacts

# Menu display and control options
while True:
    print("==============================")
    print("\nPhone Directory")
    print("1- Add new contact")
    print("2- Display all contacts")
    print("3- Search by name")
    print("4- Search by phone number")
    print("5- Save contacts to file")
    print("6- Load contacts from file")
    print("7- Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == '1':
        phonebook_module.add_contact(contacts)
    elif choice == '2':
        phonebook_module.display_contacts(contacts)
    elif choice == '3':
        phonebook_module.search_by_name(contacts)
    elif choice == '4':
        phonebook_module.search_by_phone(contacts)
    elif choice == '5':
        filename = input("Enter filename to save contacts: ")
        phonebook_module.write_to_file(contacts, filename)
        print("Contacts saved successfully.")
    elif choice == '6':
        filename = input("Enter filename to load contacts: ")
        contacts = phonebook_module.read_from_file(filename)
        print("Contacts loaded successfully.")
    elif choice == '7':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
