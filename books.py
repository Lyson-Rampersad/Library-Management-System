from data import books

# =========================================================
# This function allows management to view available books
# =========================================================

def view_list_of_books():
    """This function displays all books in the library."""
    
    print("\n==========================")
    print("List of Books")
    print("==========================")

    if len(books) == 0:

        print("No books available")
        return

    for book in books:

        print("----------------------")
        print("ISBN:", book["isbn"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Copies:", book["copies"])
        print("Branch:", book["branch"])


# =========================================================
# This function is used to add a book to the library system
# =========================================================

def issue_a_new_book():

    print("\n==========================")
    print("Add New Book")
    print("==========================")

    isbn = input("Enter ISBN (13 Digits): ")

    if len(isbn) != 13 or not isbn.isdigit():

        print("Invalid ISBN")
        return

    for book in books:

        if book["isbn"] == isbn:

            print("Book already exists")
            return

    title = input("Enter Title: ")
    author = input("Enter Author: ")
    branch = input("Enter Branch Code: ")

    while True:

        copies = input("Enter Number Of Copies: ")

        if copies.isdigit():

            copies = int(copies)
            break

        else:

            print("Enter Numbers Only")

    new_book = {

        "isbn": isbn,
        "title": title,
        "author": author,
        "copies": copies,
        "branch": branch

    }

    books.append(new_book)

    print("Book Added Successfully")


# ==========================================================================
# This function helps management search for books
# ==========================================================================

def search_for_a_book():

    isbn = input("Enter ISBN To Search: ")

    found = False

    for book in books:

        if book["isbn"] == isbn:

            found = True

            print("\nBook Found")
            print("ISBN:", book["isbn"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Copies:", book["copies"])
            print("Branch:", book["branch"])

            break

    if found == False:

        print("Book Not Found")


# =========================================================
# This function updates book information
# =========================================================

def update_book():

    print("\n==========================")
    print("Update Book")
    print("==========================")

    isbn = input("Enter ISBN: ")

    for book in books:

        if book["isbn"] == isbn:

            print("Leave Blank To Keep Current Value")

            title = input("New Title: ")
            author = input("New Author: ")

            if title != "":

                book["title"] = title

            if author != "":

                book["author"] = author

            print("Book Updated Successfully")

            return

    print("Book Not Found")


# =========================================================
# This function removes a book
# =========================================================

def remove_book_from_system():

    print("\n==========================")
    print("Remove Book")
    print("==========================")

    isbn = input("Enter ISBN: ")

    for book in books:

        if book["isbn"] == isbn:

            books.remove(book)

            print("Book Removed Successfully")

            return

    print("Book Not Found")


# =========================================================
# This function allows you to Search using title
# =========================================================

def search_book_by_title():

    title = input("Enter Book Title: ").lower()

    found = False

    for book in books:

        if title in book["title"].lower():

            found = True

            print("----------------------")
            print("ISBN:", book["isbn"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Copies:", book["copies"])

    if not found:

        print("No Matching Books Found")