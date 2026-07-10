from datetime import datetime

from data import books
from data import members
from data import loan_records
from data import branches


# =========================================================================================
# This function allows management to view reports on the library system
# =========================================================================================

def view_all_library_reports():
    """This function allows management to view reports on the library system."""

    print("\n==========================")
    print("List of Library Reports")
    print("==========================")

    print("Total Members:", len(members))
    print("Total Books:", len(books))
    print("Total Loans:", len(loan_records))

    total_copies = 0

    for book in books:

        total_copies += book["copies"]

    print("Available Copies:", total_copies)

    total_fines = 0

    for member in members.values():

        total_fines += member["outstanding_fines"]

    print("Outstanding Fines: R", round(total_fines, 2))


# ==========================================================
# Branch Report
# ==========================================================

def generate_branch_report(branch_code):
    """This function generates Branch Reports>"""

    print("\n==========================")
    print("Branch Report")
    print("==========================")

    if branch_code not in branches:

        print("Branch not found")
        return

    branch = branches[branch_code]

    print("Branch:", branch["name"])
    print("Address:", branch["address"])

    total_books = 0
    active_loans = 0
    overdue_loans = 0
    fines_issued = 0

    for book in books:

        if book["branch"] == branch_code:

            total_books += book["copies"]

    for loan in loan_records:

        member_branch = members[loan["member_id"]]["branch"]

        if member_branch == branch_code:

            active_loans += 1

            fines_issued += loan["fine_amount"]

            if loan["days_overdue"] > 0:

                overdue_loans += 1

    print("Books Available:", total_books)
    print("Loans Issued:", active_loans)
    print("Overdue Loans:", overdue_loans)
    print("Fines Issued: R", fines_issued)


# ==========================================================
# Overdue Loans
# ==========================================================

def view_overdue_loans():
    """This function allows viewing of overdue loans."""

    print("\n==========================")
    print("View List of Overdue Loans")
    print("==========================")

    found = False

    for loan in loan_records:

        if loan["days_overdue"] > 0:

            found = True

            print("--------------------------")
            print("Member ID:", loan["member_id"])
            print("ISBN:", loan["isbn"])
            print("Days Overdue:", loan["days_overdue"])
            print("Fine Amount: R", loan["fine_amount"])

    if not found:

        print("No overdue loans found")


# ==========================================================
# Cross Branch Comparison Report
# ==========================================================

def cross_branch_report():

    print("\n==========================")
    print("The Cross Branch Report")
    print("==========================")

    grand_total_loans = 0
    grand_total_fines = 0

    for branch_code, branch in branches.items():

        loan_count = 0
        fine_total = 0

        for loan in loan_records:

            member_branch = members[loan["member_id"]]["branch"]

            if member_branch == branch_code:

                loan_count += 1
                fine_total += loan["fine_amount"]

        grand_total_loans += loan_count
        grand_total_fines += fine_total

        print("--------------------------")
        print(branch["name"])
        print("Loans:", loan_count)
        print("Fines: R", fine_total)

    print("\nGRAND TOTALS")
    print("Total Loans:", grand_total_loans)
    print("Total Fines: R", grand_total_fines)


# ==========================================================
# Monthly Fine Summary
# ==========================================================

def monthly_fine_summary():

    print("\n==========================")
    print("View Monthly Fine Summary")
    print("==========================")

    total_fines = 0

    for member in members.values():

        total_fines += member["outstanding_fines"]

    print("Total Outstanding Fines: R", round(total_fines, 2))


# ==========================================================
# These are the Active Loan Statistics
# ==========================================================

def loan_statistics():
    """This functions displays the Active Loan statistics."""

    print("\n==========================")
    print("View Loan Statistics")
    print("==========================")

    active = 0
    returned = 0

    for loan in loan_records:

        if loan["return_date"] is None:

            active += 1

        else:

            returned += 1

    print("Active Loans:", active)
    print("Returned Loans:", returned)