
import json

FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone number cannot be empty.")
        return

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("This contact already exists!")
            return

    new_contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(new_contact)
    save_contacts(contacts)

    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n========== YOUR CONTACTS ==========")

    for contact in contacts:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("-----------------------------------")


def search_contact(contacts):
    name = input("Enter the name to search: ").strip().lower()

    found = False

    for contact in contacts:
        if name in contact["name"].lower():
            print("\nContact found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            found = True

    if not found:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter the exact name to delete: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n================================")
        print("        PYTHON CONTACT BOOK")
        print("================================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Thanks for using Contact Book!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
