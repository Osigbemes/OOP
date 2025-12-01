from datetime import datetime, timedelta

from books import Book
from user import User
class Loans:
    """
    Handles borrowing and returning of books.
    Tracks overdue loans.
    """

    def __init__(self):
        # Key = username, value = list of book loans
        self.borrowed = {}

    def borrow_book(self, user: User, book: Book):
        if book.available_copies <= 0:
            raise ValueError("No available copies to borrow")

        book.available_copies -= 1

        loan_record = {
            "book": book,
            "borrow_date": datetime.now(),
            "due_date": datetime.now() + timedelta(days=14)
        }

        if user.username not in self.borrowed:
            self.borrowed[user.username] = []

        self.borrowed[user.username].append(loan_record)

    def return_book(self, user: User, book: Book):
        if user.username not in self.borrowed:
            raise ValueError("User has no borrowed books")

        for loan in self.borrowed[user.username]:
            if loan["book"].book_id == book.book_id:
                self.borrowed[user.username].remove(loan)
                book.available_copies += 1
                return True

        return False

    def count_user_loans(self, user: User):
        return len(self.borrowed.get(user.username, []))

    def list_overdue_books(self):
        overdue = []
        today = datetime.now()

        for username, loans in self.borrowed.items():
            for loan in loans:
                if loan["due_date"] < today:
                    overdue.append({
                        "username": username,
                        "firstname": loan["book"].title,
                        "book": loan["book"].title,
                        "due_date": loan["due_date"]
                    })

        return overdue
