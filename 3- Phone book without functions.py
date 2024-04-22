contacts = {}  # Dictionary to store contacts

# Menu display and control options
while True:
    print("==============================")
    print("\nPhone Directory")
    print("1- Add new contact")
    print("2- Display all contacts")
    print("3- Search by name")
    print("4- Search by phone number")
    print("5- Sort contacts by name")
    print("6- Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        address = input("Enter contact address: ")
        phone = input("Enter contact phone number: ")
        birth_date = input("Enter contact birth date: ")
        contacts[name] = {'Name': name, 'Address': address, 'Phone': phone, 'Birth Date': birth_date}
    elif choice == '2':
        if contacts:
            for contact in contacts.values():
                print(contact)
        else:
            print("No contacts available.")
    elif choice == '3':
        name = input("Enter the name to search: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found.")
    elif choice == '4':
        phone = input("Enter the phone number to search: ")
        found = False
        for contact in contacts.values():
            if contact['Phone'] == phone:
                print(contact)
                found = True
                break
        if not found:
            print("Contact not found.")
    elif choice == '5':
        sorted_contacts = sorted(contacts.values(), key=lambda x: x['Name'])
        for contact in sorted_contacts:
            print(contact)
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
