#runner function, while true loop (Asking the user what they want to do)
#input statement 
#if elese for each option 

import re
import json

# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    print("\nAdd a new contact")
    identifier = input("Enter the unique identifier: ")
    if identifier in contacts:
        print("Contact with this identifier already exists.")
        return

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information: ")

    contacts[identifier] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Info": additional_info
    }
    print("Contact added successfully.")

# Function to edit an existing contact
def edit_contact():
    print("\nEdit an existing contact")
    identifier = input("Enter the unique identifier of the contact to edit: ")
    if identifier not in contacts:
        print("Contact not found.")
        return

    print(f"Editing contact: {contacts[identifier]}")
    name = input("Enter new name (leave blank to keep current): ")
    phone = input("Enter new phone number (leave blank to keep current): ")
    email = input("Enter new email address (leave blank to keep current): ")
    additional_info = input("Enter new additional information (leave blank to keep current): ")

    if name:
        contacts[identifier]["Name"] = name
    if phone:
        contacts[identifier]["Phone"] = phone
    if email:
        contacts[identifier]["Email"] = email
    if additional_info:
        contacts[identifier]["Additional Info"] = additional_info

    print("Contact updated successfully.")

# Function to delete a contact
def delete_contact():
    print("\nDelete a contact")
    identifier = input("Enter the unique identifier of the contact to delete: ")
    if identifier in contacts:
        del contacts[identifier]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# Function to search for a contact
def search_contact():
    print("\nSearch for a contact")
    identifier = input("Enter the unique identifier of the contact to search for: ")
    if identifier in contacts:
        print(f"Contact details: {contacts[identifier]}")
    else:
        print("Contact not found.")

# Function to display all contacts
def display_all_contacts():
    print("\nAll contacts:")
    for identifier, details in contacts.items():
        print(f"{identifier}: {details}")

# Function to export contacts to a text file
def export_contacts():
    print("\nExport contacts to a text file")
    filename = input("Enter the filename: ")
    with open(filename, 'w') as file:
        json.dump(contacts, file)
    print("Contacts exported successfully.")

# Function to import contacts from a text file
def import_contacts():
    print("\nImport contacts from a text file")
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            imported_contacts = json.load(file)
            contacts.update(imported_contacts)
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")

# Main menu function
def main_menu():
    while True:
        print("\nWelcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file *BONUS*")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
