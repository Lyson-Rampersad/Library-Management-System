from members import *
from books import *
from loans import *
from reports import *
from data import staff_accounts, initialise_data


# ==========================================================
# This function validates staff login details
# ==========================================================

def authenticate_staff(staff_accounts, username, password):

    if username in staff_accounts:

        if staff_accounts[username]["password"] == password:

            return staff_accounts[username]

    return None

# ==========================================================
# This function checks the login details entered by the user
# ==========================================================

def login():

    print("==========================")
    print("LIBRARY MANAGEMENT SYSTEM")
    print("==========================")

    print("Welcome To EML Library Management System")

    attempts = 0

    while attempts < 3:

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        user = authenticate_staff(
    staff_accounts,
    username,
    password
)

        if user:

            print("\nLogin Successful")
            print("Welcome", user["full_name"])

            role = user["role"]

            if role == "Librarian":

                librarian_menu()

            elif role == "Senior Librarian":

                senior_librarian_menu()

            elif role == "System Administrator":

                admin_menu()

            return

        else:

            attempts += 1

            print("Invalid Login")
            print("Attempts Remaining:", 3 - attempts)

    

    print("System Locked After 3 Failed Attempts")
    print("Login Failure Event Logged")


# ==========================================================
# Librarian Menu
# ==========================================================

def librarian_menu():
    """This function displays the librarian menu."""

    while True:

        print("\n==========================")
        print("LIBRARIAN MENU")
        print("==========================")

        print("1. Register a New Member")
        print("2. View List of Members")
        print("3. View List of Books")
        print("4. Search for a Book")
        print("5. Issue a New Book")
        print("6. Return Book")
        print("7. View All Library Reports")
        print("8. Search Member")
        print("9. Logout The System")

        choice = input("Select Option: ")

        if choice == "1":

            register_a_new_member()

        elif choice == "2":

            view_list_of_members()

        elif choice == "3":

            view_list_of_books()

        elif choice == "4":

            search_for_a_book()

        elif choice == "5":

            issue_a_new_book()

        elif choice == "6":

            return_book()

        elif choice == "7":

         view_all_library_reports()

        elif choice == "8":

         search_member()

        elif choice == "9":

         logout_the_system()

        break

    else:

     print("Invalid Option")


# ==========================================================
# Senior Librarian Menu
# ==========================================================

def senior_librarian_menu():
    """This function displays the Senior librarian menu."""



    while True:

        print("\n==========================")
        print("SENIOR LIBRARIAN MENU")
        print("==========================")

        print("1. Register a New Member")
        print("2. View List of Members")
        print("3. View List of Books")
        print("4. Search for a Book")
        print("5. Issue a New Book")
        print("6. Return Book")
        print("7. View All Library Reports")
        print("8. Search Member")
        print("9. View All Loans")
        print("10. Logout The System")

        choice = input("Select Option: ")

        if choice == "1":

            register_a_new_member()

        elif choice == "2":

            view_list_of_members()

        elif choice == "3":

            view_list_of_books()

        elif choice == "4":

            search_for_a_book()

        elif choice == "5":

            issue_a_new_book()

        elif choice == "6":

            return_book()

        elif choice == "7":

            view_all_library_reports()

        elif choice == "8":

         search_member()

        elif choice == "9":

         view_all_loans()

        elif choice == "10":

         logout_the_system()

        break


    else:

            print("Invalid Option")


# ==========================================================
# Administrator Menu
# ==========================================================

def admin_menu():
    """This function displays the Admin menu."""

    while True:

        print("\n==========================")
        print("SYSTEM ADMIN MENU")
        print("==========================")

        print("1. Register a New Member")
        print("2. View List of Members")
        print("3. View List of Books")
        print("4. Search for a Book")
        print("5. Issue a New Book")
        print("6. Return Book")
        print("7. View All Library Reports")
        print("8. Search Member")
        print("9. View All Loans")
        print("10. Logout The System")

        choice = input("Select Option: ")

        if choice == "1":

            register_a_new_member()

        elif choice == "2":

            view_list_of_members()

        elif choice == "3":

            view_list_of_books()

        elif choice == "4":

            search_for_a_book()

        elif choice == "5":

            issue_a_new_book()

        elif choice == "6":

            return_book()

        elif choice == "7":

            view_all_library_reports()

        elif choice == "8":

         search_member()

        elif choice == "9":

         view_all_loans()

        elif choice == "10":

         logout_the_system()

        break

    else:

            print("Invalid Option")


# ============================
# The Main Function
# ============================

def main():
    initialise_data()
    login()


# ============================
# This will start the program
# ============================

if __name__ == "__main__":
    main()