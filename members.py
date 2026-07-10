from data import members

# =======================================================================
# This function allows management to register a new member on the system
# =======================================================================

def register_a_new_member():

    print("\n==========================")
    print("Register a New Member")
    print("==========================")

    member_id = input("Enter Member ID: ")

    if member_id in members:

        print("Member ID already exists")
        return

    name = input("Enter Full Name: ")

    sa_id = input("Enter SA ID Number (13 Digits): ")

    if len(sa_id) != 13 or not sa_id.isdigit():

        print("Invalid SA ID")
        return

    for member in members.values():

        if member["sa_id"] == sa_id:

            print("SA ID already exists")
            return

    contact = input("Enter Contact Number: ")
    email = input("Enter Email Address: ")

    print("\nAvailable Branches")
    print("DBN001 - Durban Central Library")
    print("PIN002 - Pinetown Public Library")
    print("UML003 - Umlazi Community Library")

    branch = input("Enter Branch Code: ")

    if branch not in ["DBN001", "PIN002", "UML003"]:

        print("Invalid Branch Code")
        return

    print("\nMembership Types")
    print("1. Junior")
    print("2. Standard")
    print("3. Senior")
    print("4. Student")

    option = input("Select Membership Type: ")

    if option == "1":
        membership_type = "Junior"

    elif option == "2":
        membership_type = "Standard"

    elif option == "3":
        membership_type = "Senior"

    elif option == "4":
        membership_type = "Student"

    else:
        print("Invalid Membership Type")
        return

    members[member_id] = {

        "name": name,
        "sa_id": sa_id,
        "contact": contact,
        "email": email,
        "branch": branch,
        "membership_type": membership_type,
        "status": "Active",
        "active_loans": [],
        "outstanding_fines": 0

    }

    print("Member has been Registered Successfully")


# =================================================================
# This function allows you to view the list of members on the sytem
# =================================================================

def view_list_of_members():
    """This function allows you to view the list of members on the sytem."""

    print("\n==========================")
    print("List of Members")
    print("==========================")

    if len(members) == 0:

        print("No members found")

    else:

        for member_id, member in members.items():

            print("--------------------------")
            print("Member ID:", member_id)
            print("Name:", member["name"])
            print("Membership:", member["membership_type"])
            print("Branch:", member["branch"])
            print("Status:", member["status"])
            print("Outstanding Fines: R", member["outstanding_fines"])


# ==========================================================
# This allows staff to search for a member using member ID
# ==========================================================

def search_member():
    """This function searches for a member using the member ID."""

    member_id = input("Enter Member ID: ")

    if member_id in members:

        member = members[member_id]

        print("\nMember Found")
        print("Name:", member["name"])
        print("Membership:", member["membership_type"])
        print("Branch:", member["branch"])
        print("Outstanding Fines: R", member["outstanding_fines"])

    else:

        print("Member not found")


# ==========================================================
# This display all unique membership types using a set
# ==========================================================

def display_membership_types():
    """this function displays all unique membership types using a set."""

    membership_types = set()

    for member in members.values():
        membership_types.add(member["membership_type"])

    print("\nMembership Types In System")

    for membership in membership_types:
        print(membership)


def logout_the_system():
    print("Logging out of the system...")
    print("Goodbye!")