contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone

    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        name = input("Enter Name to Search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found")

    elif choice == "4":
        name = input("Enter Name to Delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted")
        else:
            print("Contact Not Found")

    elif choice == "5":
        break

    else:
        print("Invalid Choice")