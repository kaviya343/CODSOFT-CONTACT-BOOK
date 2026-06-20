import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    print("\nADD NEW CONTACT")

    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("\nContact Added Successfully!")


def view_contacts(contacts):
    print("\nCONTACT LIST")

    if not contacts:
        print("No contacts found.")
        return

    print("-" * 60)

    for index, contact in enumerate(contacts, start=1):
        print(
            f"{index}. {contact['name']} | {contact['phone']}"
        )


def search_contact(contacts):
    keyword = input(
        "\nEnter Name or Phone Number to Search: "
    ).lower()

    found = False

    for contact in contacts:
        if (
            keyword in contact["name"].lower()
            or
            keyword in contact["phone"]
        ):
            print("\nCONTACT FOUND")
            print("-" * 40)
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])

            found = True

    if not found:
        print("\nNo matching contact found.")


def update_contact(contacts):
    phone = input(
        "\nEnter Phone Number of Contact to Update: "
    )

    for contact in contacts:

        if contact["phone"] == phone:

            print("\nEnter New Details")

            contact["name"] = input(
                f"Name ({contact['name']}): "
            ) or contact["name"]

            contact["email"] = input(
                f"Email ({contact['email']}): "
            ) or contact["email"]

            contact["address"] = input(
                f"Address ({contact['address']}): "
            ) or contact["address"]

            save_contacts(contacts)

            print("\nContact Updated Successfully!")
            return

    print("\nContact Not Found.")


def delete_contact(contacts):
    phone = input(
        "\nEnter Phone Number to Delete: "
    )

    for contact in contacts:

        if contact["phone"] == phone:

            contacts.remove(contact)

            save_contacts(contacts)

            print("\nContact Deleted Successfully!")
            return

    print("\nContact Not Found.")


def main():

    contacts = load_contacts()

    while True:

        print("\n" + "=" * 60)
        print("        SMART CONTACT BOOK")
        print("=" * 60)

        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter Choice (1-6): ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("\nThank You For Using Contact Book!")
            break

        else:
            print("\nInvalid Choice!")


main()
