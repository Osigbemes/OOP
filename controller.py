from datetime import datetime
from books import Book
from booklist import BookList
from user import User
from userlist import UserList
from loans import Loans


class CLIController:
    """
    Command Line Interface for Library System.
    Handles user interaction and routes commands to the domain classes.
    """

    def __init__(self):
        # Collections
        self.books = BookList()
        self.users = UserList()
        self.loans = Loans()
        self.current_user = None

    # ================= RUN LOOP =================
    def run(self):
        while True:
            if not self.current_user:
                self.auth_menu()
            else:
                self.main_menu()

    # ================= AUTH MENU =================
    def auth_menu(self):
        print("\n=== LIBRARY SYSTEM ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            self.login()
        elif choice == "2":
            self.register()
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice!")

    def login(self):
        username = input("Username: ")
        user = self.users.get_user_by_username(username)
        if user:
            self.current_user = user
            print(f"Welcome back, {user.get_firstname()}!")
        else:
            print("User not found. Please register first.")

    def register(self):
        username = input("Username: ")
        firstname = input("First Name: ")
        surname = input("Surname: ")
        house_no = input("House Number: ")
        street = input("Street: ")
        postcode = input("Postcode: ")
        email = input("Email: ")
        dob_str = input("Date of Birth (YYYY-MM-DD): ")
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format!")
            return

        user = User(username, firstname, surname, house_no, street, postcode, email, str(dob))
        self.users.add_user(user)
        self.current_user = user
        print(f"User {firstname} registered successfully!")

    # ================= MAIN MENU =================
    def main_menu(self):
        if self.current_user.get_username() == "admin":  # Simple admin check
            self.admin_menu()
        else:
            self.member_menu()

    # ================= ADMIN MENU =================
    def admin_menu(self):
        print("\n=== ADMIN MENU ===")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. View All Books")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            self.add_book()
        elif choice == "2":
            self.update_book()
        elif choice == "3":
            self.delete_book()
        elif choice == "4":
            self.books_list()
        elif choice == "5":
            self.current_user = None
        else:
            print("Invalid choice!")

    def add_book(self):
        title = input("Title: ")
        author = input("Author: ")
        year = input("Year: ")
        publisher = input("Publisher: ")
        copies = input("Total Copies: ")
        pub_date_str = input("Publication Date (YYYY-MM-DD): ")

        try:
            pub_date = datetime.strptime(pub_date_str, "%Y-%m-%d").date()
            book = Book(title, author, year, publisher, copies, pub_date)
            self.books.add_book(book)
            print(f"Book '{title}' added successfully!")
        except Exception as e:
            print(f"Error adding book: {e}")

    def update_book(self):
        title = input("Title of book to update: ")
        book = self.books.search_book(title=title)
        if not book:
            print("Book not found!")
            return

        new_title = input("New Title (Enter to skip): ") or None
        new_author = input("New Author (Enter to skip): ") or None
        new_year = input("New Year (Enter to skip): ") or None
        new_publisher = input("New Publisher (Enter to skip): ") or None
        new_copies = input("New Total Copies (Enter to skip): ") or None

        try:
            if new_title: book.set_title(new_title)
            if new_author: book.set_author(new_author)
            if new_year: book.set_year(new_year)
            if new_publisher: book.set_publisher(new_publisher)
            if new_copies: book.set_total_copies(new_copies)
            print("Book updated successfully!")
        except Exception as e:
            print(f"Error updating book: {e}")

    def delete_book(self):
        title = input("Title of book to delete: ")
        if self.books.remove_book_by_title(title):
            print("Book deleted successfully!")
        else:
            print("Book not found!")

    def books_list(self):
        print("\n=== ALL BOOKS ===")
        for book in self.books.books.values():
            print(f"{book.get_title()} by {book.get_author()} ({book.get_year()}) - {book.get_available_copies()}/{book.get_total_copies()} available")

    # ================= MEMBER MENU =================
    def member_menu(self):
        print("\n=== MEMBER MENU ===")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View My Borrowed Books")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            self.books_list()
        elif choice == "2":
            self.borrow_book()
        elif choice == "3":
            self.return_book()
        elif choice == "4":
            self.view_my_loans()
        elif choice == "5":
            self.current_user = None
        else:
            print("Invalid choice!")

    def borrow_book(self):
        title = input("Book Title to Borrow: ")
        book = self.books.search_book(title=title)
        if not book:
            print("Book not found!")
            return

        try:
            self.loans.borrow_book(self.current_user, book)
            print(f"You have borrowed '{book.get_title()}'")
        except Exception as e:
            print(f"Error: {e}")

    def return_book(self):
        title = input("Book Title to Return: ")
        book = self.books.search_book(title=title)
        if not book:
            print("Book not found!")
            return

        try:
            if self.loans.return_book(self.current_user, book):
                print(f"You returned '{book.get_title()}'")
            else:
                print("You haven't borrowed this book.")
        except Exception as e:
            print(f"Error: {e}")

    def view_my_loans(self):
        print("\n=== MY BORROWED BOOKS ===")
        count = self.loans.count_user_loans(self.current_user)
        print(f"You currently have {count} borrowed book(s).")
        for loans in self.loans.borrowed.get(self.current_user.get_username(), []):
            book = loans["book"]
            due = loans["due_date"]
            print(f"{book.get_title()} - Due: {due.date()}")


# =============================
# RUN THE APPLICATION
# =============================
if __name__ == "__main__":
    CLIController().run()
