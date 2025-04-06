def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input()        
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input()
    email = input()
    address = input()
    contact_book[name] = {
        "phone": phone,
        "email":email,
        "address": address
    }
    print("Contact added successfully!")

def view_contact(contact_book):
    name = input()
    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input()

    # It checks if the provided name exits in the dictionry
    if name in contact_book:

        # It promts the user to enter new values
        phone = input()
        email = input()
        address = input()

        # It checks if the user pressed Enter without providing any input
        if phone == '':
            phone = contact_book[name]['phone']
        if email == '':
            email = contact_book[name]['email']
        if address == '':
            address = contact_book[name]['address']

        # Update the contact's information in the dictionary
        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found!")
        
display_menu()
add_contact()
edit_contact()
view_contact()