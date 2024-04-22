import json

def add_contact(contacts):
    name = input("Enter contact name: ")
    address = input("Enter contact address: ")
    phone = input("Enter contact phone number: ")
    birth_date = input("Enter contact birth date: ")
    contacts[name] = {'Name': name, 'Address': address, 'Phone': phone, 'Birth Date': birth_date}

def search_by_name(contacts):
    name = input("Enter the name to search: ")
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def search_by_phone(contacts):
    phone = input("Enter the phone number to search: ")
    found = False
    for contact in contacts.values():
        if contact['Phone'] == phone:
            print(contact)
            found = True
            break
    if not found:
        print("Contact not found.")

def display_contacts(contacts):
    if contacts:
        for contact in contacts.values():
            print(contact)
    else:
        print("No contacts available.")

def write_to_file(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

def read_from_file(filename):
    with open(filename, 'r') as file:
        contacts = json.load(file)
    return contacts
