import json
import os

# ================= COLORS =================
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

FILE_NAME = "contacts.json"


# ================= DATABASE =================
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# ================= DASHBOARD =================
def dashboard(contacts):
    total = len(contacts)
    favorites = sum(1 for c in contacts if c["favorite"])

    print(f"\n{CYAN}{'='*65}")
    print("📒 CONTACT HUB PRO")
    print(f"{'='*65}")
    print(f"👥 Total Contacts : {total}")
    print(f"⭐ Favorite Contacts : {favorites}")
    print(f"{'='*65}{RESET}")


# ================= ID GENERATOR =================
def generate_contact_id(contacts):
    return f"C{len(contacts)+1:03d}"


# ================= ADD CONTACT =================
def add_contact(contacts):

    print(f"\n{GREEN}ADD NEW CONTACT{RESET}")

    name = input("Name       : ")
    phone = input("Phone      : ")
    email = input("Email      : ")
    address = input("Address    : ")

    favorite = input(
        "Favorite Contact? (yes/no): "
    ).lower()

    contact = {
        "id": generate_contact_id(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "favorite": favorite == "yes"
    }

    contacts.append(contact)
    save_contacts(contacts)

    print(f"\n{GREEN}✓ Contact Added Successfully!{RESET}")


# ================= VIEW CONTACTS =================
def view_contacts(contacts):

    if not contacts:
        print(f"\n{RED}No Contacts Found!{RESET}")
        return

    print(f"\n{BLUE}{'-'*85}")
    print(
        f"{'ID':<8}{'NAME':<20}{'PHONE':<18}{'FAVOURITE':<12}"
    )
    print(f"{'-'*85}{RESET}")

    for contact in contacts:

        fav = "⭐" if contact["favorite"] else "-"

        print(
            f"{contact['id']:<8}"
            f"{contact['name']:<20}"
            f"{contact['phone']:<18}"
            f"{fav:<12}"
        )


# ================= SEARCH =================
def search_contact(contacts):

    keyword = input(
        "\nEnter Name / Phone / Email: "
    ).lower()

    found = False

    for contact in contacts:

        if (
            keyword in contact["name"].lower()
            or keyword in contact["phone"]
            or keyword in contact["email"].lower()
        ):

            print(f"\n{YELLOW}{'-'*40}")
            print("CONTACT FOUND")
            print(f"{'-'*40}{RESET}")

            print("ID       :", contact["id"])
            print("Name     :", contact["name"])
            print("Phone    :", contact["phone"])
            print("Email    :", contact["email"])
            print("Address  :", contact["address"])
            print(
                "Favorite :",
                "Yes ⭐" if contact["favorite"] else "No"
            )

            found = True

    if not found:
        print(f"\n{RED}✗ Contact Not Found!{RESET}")


# ================= UPDATE =================
def update_contact(contacts):

    contact_id = input(
        "\nEnter Contact ID to Update: "
    ).upper()

    for contact in contacts:

        if contact["id"] == contact_id:

            print(f"\n{CYAN}Enter New Details{RESET}")

            contact["name"] = (
                input(
                    f"Name ({contact['name']}): "
                )
                or contact["name"]
            )

            contact["phone"] = (
                input(
                    f"Phone ({contact['phone']}): "
                )
                or contact["phone"]
            )

            contact["email"] = (
                input(
                    f"Email ({contact['email']}): "
                )
                or contact["email"]
            )

            contact["address"] = (
                input(
                    f"Address ({contact['address']}): "
                )
                or contact["address"]
            )

            save_contacts(contacts)

            print(
                f"\n{GREEN}✓ Contact Updated Successfully!{RESET}"
            )
            return

    print(f"\n{RED}✗ Contact Not Found!{RESET}")


# ================= DELETE =================
def delete_contact(contacts):

    contact_id = input(
        "\nEnter Contact ID to Delete: "
    ).upper()

    for contact in contacts:

        if contact["id"] == contact_id:

            contacts.remove(contact)

            save_contacts(contacts)

            print(
                f"\n{GREEN}✓ Contact Deleted Successfully!{RESET}"
            )
            return

    print(f"\n{RED}✗ Contact Not Found!{RESET}")


# ================= FAVORITES =================
def view_favorites(contacts):

    favorites = [
        c for c in contacts if c["favorite"]
    ]

    if not favorites:
        print(
            f"\n{RED}No Favorite Contacts Found!{RESET}"
        )
        return

    print(f"\n{MAGENTA}⭐ FAVORITE CONTACTS{RESET}")

    for contact in favorites:

        print(
            f"{contact['id']} - "
            f"{contact['name']} "
            f"({contact['phone']})"
        )


# ================= MAIN =================
def main():

    contacts = load_contacts()

    while True:

        dashboard(contacts)

        print(f"{GREEN}1. Add Contact{RESET}")
        print(f"{BLUE}2. View Contacts{RESET}")
        print(f"{YELLOW}3. Search Contact{RESET}")
        print(f"{CYAN}4. Update Contact{RESET}")
        print(f"{MAGENTA}5. Delete Contact{RESET}")
        print(f"{GREEN}6. Favorite Contacts{RESET}")
        print(f"{RED}7. Exit{RESET}")

        choice = input(
            "\nEnter Choice (1-7): "
        )

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
            view_favorites(contacts)

        elif choice == "7":
            print(
                f"\n{GREEN}Thank You For Using Contact Hub Pro!{RESET}"
            )
            break

        else:
            print(
                f"\n{RED}Invalid Choice! Try Again.{RESET}"
            )


main()
