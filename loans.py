from datetime import datetime, timedelta

from data import books
from data import members
from data import loan_records
from data import MEMBERSHIP_RULES


# ===================================================
# This function calculates fines
# ===================================================

# ===================================================
# Fine Strategy Functions
# ===================================================

def junior_fine(days_overdue, first_offence):
    """
    Junior members:
    First offence = no fine
    Thereafter R1 per day
    """

    if first_offence:
        return 0

    return days_overdue * 1


def standard_fine(days_overdue, num_books):
    """
    Standard members:
    R2.50 per day per book
    """

    return days_overdue * 2.50 * num_books


def senior_fine(days_overdue, num_books):
    """
    Senior members:
    R1 per day per book
    Maximum R30 per book
    """

    fine_per_book = days_overdue * 1

    if fine_per_book > 30:
        fine_per_book = 30

    return fine_per_book * num_books


def student_fine(days_overdue, num_books):
    """
    Student members:
    R1.50 per day per book
    """

    return days_overdue * 1.50 * num_books


# ===================================================
# Main Fine Calculator
# ===================================================

def calculate_fine(
        membership_type,
        days_overdue,
        num_books,
        first_offence=False
):
    """
    Calculate library fine according
    to membership type.

    Returns:
        float
    """

    if days_overdue <= 0:
        return 0

    if membership_type == "Junior":

        return junior_fine(
            days_overdue,
            first_offence
        )

    elif membership_type == "Standard":

        return standard_fine(
            days_overdue,
            num_books
        )

    elif membership_type == "Senior":

        return senior_fine(
            days_overdue,
            num_books
        )

    elif membership_type == "Student":

        return student_fine(
            days_overdue,
            num_books
        )

    return 0


# ===================================================
# This function is used by management to issue a book
# ===================================================

def issue_a_new_book():

    print("\n==========================")
    print("Issue New Book")
    print("==========================")

    member_id = input("Enter Member ID: ")

    if member_id not in members:

        print("Member not found")
        return

    isbn = input("Enter ISBN: ")

    selected_book = None

    for book in books:

        if book["isbn"] == isbn:

            selected_book = book
            break

    if selected_book is None:

        print("Book not found")
        return

    if selected_book["copies"] <= 0:

        print("No copies available")
        return

    member = members[member_id]

    if member["outstanding_fines"] > 50:

        print("Member has outstanding fines above R50")
        return

    membership_type = member["membership_type"]

    max_books = MEMBERSHIP_RULES[membership_type]["limit"]

    if len(member["active_loans"]) >= max_books:

        print("Loan limit reached")
        return

    issue_date = datetime.now()

    loan_period = MEMBERSHIP_RULES[membership_type]["period"]

    due_date = issue_date + timedelta(days=loan_period)

    loan = {

    "loan_id": len(loan_records) + 1,
    "member_id": member_id,
    "isbn": isbn,
    "branch_code": member["branch"],
    "issue_date": issue_date,
    "due_date": due_date,
    "return_date": None,
    "days_overdue": 0,
    "fine_amount": 0,
    "fine_paid": False

}
    loan_records.append(loan)

    member["active_loans"].append(isbn)

    selected_book["copies"] -= 1

    print("\nLoan Successful")
    print("Due Date:", due_date.strftime("%d/%m/%Y"))


# ===================================================
# This function is used when returning a book
# ===================================================

def return_book():

    print("\n==========================")
    print("Return Book")
    print("==========================")

    member_id = input("Enter Member ID: ")
    isbn = input("Enter ISBN: ")

    found = False

    for loan in loan_records:

        if loan["member_id"] == member_id and loan["isbn"] == isbn and loan["return_date"] is None:

            found = True

            return_date = datetime.now()

            loan["return_date"] = return_date

            days_overdue = (return_date - loan["due_date"]).days

            if days_overdue < 0:
                days_overdue = 0

            loan["days_overdue"] = days_overdue

            membership_type = members[member_id]["membership_type"]

            fine = calculate_fine(
                membership_type,
                days_overdue,
                1
            )

            loan["fine_amount"] = fine

            members[member_id]["outstanding_fines"] += fine

            if isbn in members[member_id]["active_loans"]:
                members[member_id]["active_loans"].remove(isbn)

            for book in books:

                if book["isbn"] == isbn:

                    book["copies"] += 1
                    break

            print("\nBook Returned Successfully")
            print("Days Overdue:", days_overdue)
            print("Fine Amount: R", fine)

            break

    if not found:

        print("Loan record not found")


# ===================================================
# View all active loans
# ===================================================

def view_all_loans():

    print("\n==========================")
    print("Active Loan Record")
    print("==========================")

    if len(loan_records) == 0:

        print("No loan records available")
        return

    for loan in loan_records:

        print("--------------------------")
        print("Loan ID:", loan["loan_id"])
        print("Member ID:", loan["member_id"])
        print("ISBN:", loan["isbn"])

        if "branch_code" in loan:
            print("Branch Code:", loan["branch_code"])

        print("Issue Date:",
              loan["issue_date"].strftime("%d/%m/%Y"))

        print("Due Date:",
              loan["due_date"].strftime("%d/%m/%Y"))

        if loan["return_date"] is None:

            print("Return Date: Not Returned")

        else:

            print("Return Date:",
                  loan["return_date"].strftime("%d/%m/%Y"))

        print("Days Overdue:",
              loan["days_overdue"])

        print("Fine Amount: R",
              loan["fine_amount"])

        print("Fine Paid:",
              loan["fine_paid"])
