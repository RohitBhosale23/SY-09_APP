from Book import Book
from user import User
from datetime import datetime


class Transaction:

    def __init__(self):
        self.users = []
        self.books = []

    # Add User
    def add_user(self):
        user_id = input("Enter User ID : ")
        name = input("Enter Name : ")
        email = input("Enter Email : ")

        user = User(user_id, name, email)
        self.users.append(user)

        print("\nUser Added Successfully\n")

    # Add Book
    def add_book(self):
        book_id = input("Enter Book ID : ")
        title = input("Enter Book Title : ")
        author = input("Enter Author Name : ")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("\nBook Added Successfully\n")

    # Show Users
    def show_users(self):
        if len(self.users) == 0:
            print("\nNo Users Found\n")
            return

        for user in self.users:
            user.display()

    # Show Books
    def show_books(self):
        if len(self.books) == 0:
            print("\nNo Books Available\n")
            return

        for book in self.books:
            book.display()

    # Search Book
    def search_book(self):
        title = input("Enter Book Title : ")

        for book in self.books:
            if book.title.lower() == title.lower():
                book.display()
                return

        print("\nBook Not Found\n")

    # Issue Book
    def issue_book(self):
        book_id = input("Enter Book ID : ")

        for book in self.books:
            if book.book_id == book_id:

                if book.available:
                    issuer = input("Enter Issuer Name : ")

                    book.available = False
                    book.issued_to = issuer
                    book.issue_date = datetime.now().strftime("%d-%m-%Y")

                    print("\nBook Issued Successfully")
                    print("Issued To :", book.issued_to)
                    print("Issue Date:", book.issue_date)
                    print()

                else:
                    print("\nBook Already Issued")
                    print("Issued To :", book.issued_to)
                    print("Issue Date:", book.issue_date)
                    print()

                return

        print("\nBook Not Found\n")

    # Return Book
    def return_book(self):
        book_id = input("Enter Book ID : ")

        for book in self.books:
            if book.book_id == book_id:

                if not book.available:
                    book.available = True
                    book.issued_to = None
                    book.issue_date = None

                    print("\nBook Returned Successfully\n")

                else:
                    print("\nBook is Already Available\n")

                return

        print("\nBook Not Found\n")

    # Update User
    def update_user(self):
        user_id = input("Enter User ID to Update : ")

        for user in self.users:
            if user.user_id == user_id:
                user.name = input("Enter New Name : ")
                user.email = input("Enter New Email : ")

                print("\nUser Updated Successfully\n")
                return

        print("\nUser Not Found\n")

    # Delete User
    def delete_user(self):
        user_id = input("Enter User ID to Delete : ")

        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)

                print("\nUser Deleted Successfully\n")
                return

        print("\nUser Not Found\n")

    # Update Book
    def update_book(self):
        book_id = input("Enter Book ID to Update : ")

        for book in self.books:
            if book.book_id == book_id:
                book.title = input("Enter New Book Title : ")
                book.author = input("Enter New Author Name : ")

                print("\nBook Updated Successfully\n")
                return

        print("\nBook Not Found\n")

    # Delete Book
    def delete_book(self):
        book_id = input("Enter Book ID to Delete : ")

        for book in self.books:
            if book.book_id == book_id:

                if not book.available:
                    print("\nCannot Delete. Book is Currently Issued.\n")
                    return

                self.books.remove(book)

                print("\nBook Deleted Successfully\n")
                return

        print("\nBook Not Found\n")


if __name__ == "__main__":

    library = Transaction()

    while True:

        print("\n========== Library Management System ==========")
        print("1. Add User")
        print("2. Add Book")
        print("3. Show Users")
        print("4. Show Books")
        print("5. Search Book")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Update User")
        print("9. Update Book")
        print("10. Delete User")
        print("11. Delete Book")
        print("12. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            library.add_user()

        elif choice == "2":
            library.add_book()

        elif choice == "3":
            library.show_users()

        elif choice == "4":
            library.show_books()

        elif choice == "5":
            library.search_book()

        elif choice == "6":
            library.issue_book()

        elif choice == "7":
            library.return_book()

        elif choice == "8":
            library.update_user()

        elif choice == "9":
            library.update_book()

        elif choice == "10":
            library.delete_user()

        elif choice == "11":
            library.delete_book()

        elif choice == "12":
            print("\nThank You...")
            break

        else:
            print("\nInvalid Choice\n")