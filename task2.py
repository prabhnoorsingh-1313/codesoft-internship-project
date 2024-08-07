
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        print("Contact List:")
        for name, details in self.contacts.items():
            print(f"{name}: {details['phone']}")

    def search_contact(self, query):
        for name, details in self.contacts.items():
            if query in name or query in details["phone"]:
                print(f"{name}: {details['phone']}")
                return
        print("Contact not found!")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address
            print(f"Contact '{name}' updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Contact not found!")


def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)
        elif choice == "4":
            name = input("Enter name: ")
            phone = input("Enter new phone number (optional): ")
            email = input("Enter new email (optional): ")
            address = input("Enter new address (optional): ")
            contact_book.update_contact(name, phone or None, email or None, address or None)
        elif choice == "5":
            name = input("Enter name: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
