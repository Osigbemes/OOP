from datetime import datetime, timedelta
from books import Book
from user import User


class Loans:
    """
    Handles borrowing and returning of books in the library system.
    Also tracks overdue books.
    """

    def __init__(self):
        """
        Constructor to create a new Loans object.
        Stores borrowed books using a dictionary.
        Key   -> username
        Value -> list of loan records
        """
        self.borrowed = {}

    def borrow_book(self, user: User, book: Book):
        """
        Allows a user to borrow a book if copies are available.
        """

        if not isinstance(user, User):
            raise TypeError("Invalid user object")

        if not isinstance(book, Book):
            raise TypeError("Invalid book object")

        if book.get_available_copies() <= 0:
            raise ValueError("No available copies to borrow")

        # Reduce available copies
        book.available_copies -= 1

        loan_record = {
            "user": user,
            "book": book,
            "borrow_date": datetime.now(),
            "due_date": datetime.now() + timedelta(days=14)
        }

        if user.get_username() not in self.borrowed:
            self.borrowed[user.get_username()] = []

        self.borrowed[user.get_username()].append(loan_record)

    def return_book(self, user: User, book: Book):
        """
        Allows a user to return a previously borrowed book.
        """

        if user.get_username() not in self.borrowed:
            raise ValueError("User has no borrowed books")

        for loan in self.borrowed[user.get_username()]:
            if loan["book"].get_title() == book.get_title():
                self.borrowed[user.get_username()].remove(loan)
                book.available_copies += 1
                return True

        raise ValueError("This book was not borrowed by the user")

    def count_user_loans(self, user: User):
        """
        Returns the total number of books currently borrowed by a user.
        """
        return len(self.borrowed.get(user.get_username(), []))

    def list_overdue_books(self):
        """
        Returns a list of overdue books with user's username and first name.
        """
        today = datetime.now()
        overdue_records = []

        for loans in self.borrowed.values():
            for loan in loans:
                if loan["due_date"] < today:
                    user: User = loan["user"]
                    book: Book = loan["book"]

                    overdue_records.append({
                        "username": user.get_username(),
                        "firstname": user.get_firstname(),
                        "book": book.get_title(),
                        "due_date": loan["due_date"].date()
                    })

        return overdue_records

