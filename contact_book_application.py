import json
import re

# Function to validate email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Load contacts from a JSON file
def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to a JSON file
def save_contacts(contact_book):
    with open('contacts.json', 'w') as file:
        json.dump(contact_book, file, indent=4)

# Display the main menu
def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
    return input("Select an option (1-6): ")

# Add a new contact
def add_contact(contact_book):
    name = input("Enter the contact name: ").strip().lower()
    if name in contact_book:
        print("Contact already exists!")
        return
    
    phone = input("Enter phone number: ").strip()
    if not phone.isdigit():
        print("Invalid phone number. Only digits are allowed.")
        return
    
    email = input("Enter email: ").strip()
    if not is_valid_email(email):
        print("Invalid email format.")
        return

    address = input("Enter address: ").strip()

    contact_book[name] = {
        "name": name.title(),
        "phone": phone,
        "email": email,
        "address": address
    }
    save_contacts(contact_book)
    print("Contact added successfully!")

# View contact details
def view_contact(contact_book):
    name = input("Enter the contact name to view: ").strip().lower()
    contact = contact_book.get(name)
    if contact:
        print(f"\nName: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found!")

# Edit an existing contact
def edit_contact(contact_book):
    name = input("Enter the contact name to edit: ").strip().lower()
    if name in contact_book:
        contact = contact_book[name]
        print("Press Enter to keep the current value.")

        phone = input(f"Enter new phone number ({contact['phone']}): ").strip()
        email = input(f"Enter new email ({contact['email']}): ").strip()
        address = input(f"Enter new address ({contact['address']}): ").strip()

        # Update only if new values are provided
        contact['phone'] = phone if phone else contact['phone']
        contact['email'] = email if email else contact['email']
        contact['address'] = address if address else contact['address']

        contact_book[name] = contact
        save_contacts(contact_book)
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

# Delete a contact
def delete_contact(contact_book):
    name = input("Enter the contact name to delete: ").strip().lower()
    if name in contact_book:
        del contact_book[name]
        save_contacts(contact_book)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# List all contacts
def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        print("\nAll Contacts:")
        for contact in contact_book.values():
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("-" * 20)

# Main program loop
if __name__ == "__main__":
    contact_book = load_contacts()

    while True:
        choice = display_menu()

        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contact(contact_book)
        elif choice == '3':
            edit_contact(contact_book)
        elif choice == '4':
            delete_contact(contact_book)
        elif choice == '5':
            list_all_contacts(contact_book)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
