from books import Book, BorrowRecord
from user import User


class AuthService:
    def __init__(self):
        self.users = {}
        self._seed_admin()

    def _seed_admin(self):
        self.users["admin"] = User("admin", "System Admin", "admin@lib.com", "admin123", role="admin")

    def register(self, user_id, name, email, password):
        if user_id in self.users:
            print("User ID already exists!")
            return None

        user = User(user_id, name, email, password)
        self.users[user_id] = user
        print("Registration successful!")
        return user

    def login(self, user_id, password):
        user = self.users.get(user_id)
        if not user or user.password != password:
            print("Invalid credentials!")
            return None
        return user


class LibraryService:
    def __init__(self):
        self.books = {}
        self.borrow_records = {}
        self.record_counter = 1

    # -------- BOOK MANAGEMENT --------
    def add_book(self, book_id, title, author, quantity):
        if book_id in self.books:
            print("Book ID already exists!")
            return

        self.books[book_id] = Book(title, author, '', '', quantity, book_id=book_id)
        print("Book added successfully!")

    def update_book(self, book_id, title=None, author=None, quantity=None):
        book: Book = self.books.get(book_id)
        if not book:
            print("Book not found!")
            return

        if title:
            book.title = title
        if author:
            book.author = author
        if quantity is not None:
            book.set_quantity(quantity)

        print("Book updated successfully!")

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book deleted!")
        else:
            print("Book not found!")

    def list_books(self):
        print("\n=== BOOK LIST ===")
        for b in self.books.values():
            print(f"{b.book_id} | {b.title} | {b.author} | Qty: {b.quantity}")
        print()


    # -------- BORROW / RETURN --------
    def borrow_book(self, user_id, book_id):
        book : Book = self.books.get(book_id)
        if not book:
            print("Book not found!")
            return
        
        if book.total_copies < 1:
            print("Book is unavailable!")
            return

        book.total_copies -= 1
        record = BorrowRecord(self.record_counter, user_id, book_id)
        self.borrow_records[self.record_counter] = record
        self.record_counter += 1

        print("Book borrowed successfully!")

    def return_book(self, record_id):
        record = self.borrow_records.get(record_id)
        if not record:
            print("Borrow record not found!")
            return

        book : Book = self.books.get(record.book_id)
        book.total_copies += 1

        del self.borrow_records[record_id]
        print("Book returned successfully!")

    def list_borrowed(self, user_id):
        print("\n=== BORROWED BOOKS ===")
        for r in self.borrow_records.values():
            if r.user_id == user_id:
                book : Book = self.books[r.book_id]
                print(f"Record {r.record_id} | {book.title} ({book.book_id})")
        print()