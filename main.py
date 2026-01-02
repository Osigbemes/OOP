"""
main.py
--------
Command Line Interface for the Library Record System.
Provides menu-driven interaction for managing books, users, and loans.
"""

from datetime import datetime
from books import Book
from booklist import BookList
from user import User
from userlist import UserList
from loans import Loans

def read_date(prompt):
        """
        Reads a date string from CLI and converts it to a date object.
        """
        while True:
            user_input = input(prompt)
            try:
                return datetime.strptime(user_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

class LibraryCLI:
    """
    Main CLI controller for the Library System.
    """

    def __init__(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.loans = Loans()

    # ================= MAIN MENU =================
    def run(self):
        while True:
            print("\n====== LIBRARY SYSTEM ======")
            print("1. Manage Books")
            print("2. Manage Users")
            print("3. Loans")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.book_menu()
            elif choice == "2":
                self.user_menu()
            elif choice == "3":
                self.loan_menu()
            elif choice == "4":
                print("Exiting system...")
                break
            else:
                print("Invalid choice. Please try again.")

    # ================= BOOK MENU =================
    def book_menu(self):
        print("\n--- BOOK MANAGEMENT ---")
        print("1. Add Book")
        print("2. Modify Book")
        print("3. Remove Book")
        print("4. View Total Books")
        print("5. Back")

        choice = input("Choose: ")

        if choice == "1":
            self.add_book()
        elif choice == "2":
            self.modify_book()
        elif choice == "3":
            self.remove_book()
        elif choice == "4":
            print(f"Total books: {self.book_list.count_books()}")
        elif choice == "5":
            return
        else:
            print("Invalid option")
            
    def read_date(self, prompt="Enter date (YYYY-MM-DD): "):
        """
        Reads a date string from CLI and converts it to a date object.
        """
        while True:
            user_input = input(prompt)
            try:
                return datetime.strptime(user_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def add_book(self):
        try:
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            publisher = input("Publisher: ")
            copies = input("Number of copies: ")
            pub_date = self.read_date("New publication date (YYYY-MM-DD): ")

            book = Book(title, author, year, publisher, copies, pub_date)
            self.book_list.add_book(book)
            print("Book added successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def modify_book(self):
        title = input("Enter book title | author | year to modify: ")
        book = self.book_list.search_book(title=title)

        if not book:
            print("Book not found.")
            return

        print("""
        1. Title
        2. Author
        3. Year
        4. Publisher
        5. Number of copies
        """)

        choice = input("Choose field to modify: ")

        try:
            if choice == "1":
                book.set_title(input("New title: "))
            elif choice == "2":
                book.set_author(input("New author: "))
            elif choice == "3":
                book.set_year(input("New year: "))
            elif choice == "4":
                book.set_publisher(input("New publisher: "))
            elif choice == "5":
                book.set_total_copies(input("New number of copies: "))
            else:
                print("Invalid choice")
                return

            print("Book updated successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def remove_book(self):
        title = input("Enter book title to remove: ")
        if self.book_list.remove_book_by_title(title):
            print("Book removed.")
        else:
            print("Book not found.")

    # ================= USER MENU =================
    def user_menu(self):
        print("\n--- USER MANAGEMENT ---")
        print("1. Add User")
        print("2. Modify User")
        print("3. Remove User (by first name)")
        print("4. Count Users")
        print("5. Back")

        choice = input("Choose: ")

        if choice == "1":
            self.add_user()
        elif choice == "2":
            self.modify_user()
        elif choice == "3":
            print(self.user_list.remove_user_by_firstname(
                input("First name: ")
            ))
        elif choice == "4":
            print(f"Total users: {self.user_list.count_users()}")
        elif choice == "5":
            return
        else:
            print("Invalid option")

    def add_user(self):
        try:
            user = User(
                username=input("Username: "),
                firstname=input("First name: "),
                surname=input("Surname: "),
                house_no=input("House number: "),
                street=input("Street name: "),
                postcode=input("Postcode: "),
                email=input("Email: "),
                dob=str(read_date("Date of Birth (YYYY-MM-DD): "))
            )
            self.user_list.add_user(user)
            print("User added successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def modify_user(self):
        username = input("Enter username: ")
        user = self.user_list.get_user_by_username(username)

        if not user:
            print("User not found.")
            return

        print("""
        1. First name
        2. Surname
        3. House number
        4. Street name
        5. Postcode
        """)

        choice = input("Choose field to modify: ")

        if choice == "1":
            user.edit_firstname(input("New first name: "))
        elif choice == "2":
            user.edit_surname(input("New surname: "))
        elif choice == "3":
            user.edit_house_number(input("New house number: "))
        elif choice == "4":
            user.edit_street_name(input("New street name: "))
        elif choice == "5":
            user.edit_postcode(input("New postcode: "))
        else:
            print("Invalid choice")
            return

        print("User updated successfully.")

    # ================= LOANS MENU =================
    def loan_menu(self):
        print("\n--- LOANS ---")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. Count User Loans")
        print("4. List Overdue Books")
        print("5. Back")

        choice = input("Choose: ")

        try:
            if choice == "1":
                user = self.user_list.get_user_by_username(
                    input("Username: ")
                )
                book = self.book_list.search_book(
                    title=input("Book title: ")
                )
                self.loans.borrow_book(user, book)
                print("Book borrowed successfully.")

            elif choice == "2":
                user = self.user_list.get_user_by_username(
                    input("Username: ")
                )
                book = self.book_list.search_book(
                    title=input("Book title: ")
                )
                self.loans.return_book(user, book)
                print("Book returned.")

            elif choice == "3":
                user = self.user_list.get_user_by_username(
                    input("Username: ")
                )
                print(
                    "Books borrowed:",
                    self.loans.count_user_loans(user)
                )

            elif choice == "4":
                records = self.loans.list_overdue_books()

                if not records:
                    print("No overdue books found.")
                else:
                    for record in records:
                        print(
                            f"Username: {record['username']}, "
                            f"First name: {record['firstname']}, "
                            f"Book: {record['book']}, "
                            f"Due date: {record['due_date']}"
                        )


            elif choice == "5":
                return

            else:
                print("Invalid choice")
        except Exception as e:
            print(f"Error: {e}")


# ================= RUN APPLICATION =================
if __name__ == "__main__":
    LibraryCLI().run()


