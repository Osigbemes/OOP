from books import Book

class BookList:
    """
    Stores and manages a collection of Book objects.
    Uses a dictionary with key = book_id, value = Book instance.
    """

    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        self.books[book.book_id] = book

    def search(self, **kwargs):
        """
        Search by: title, author, publisher, publication_date
        Example: search(title="Harry Potter")
        """
        if not kwargs:
            raise ValueError("You must provide a search field")

        key, value = list(kwargs.items())[0]

        for book in self.books.values():
            if getattr(book, key, None) == value:
                return book

        return None

    def remove_book_by_title(self, title):
        for book_id, book in (self.books.items()):
            if book.title == title:
                del self.books[book_id]
                return True
        return False

    def count_books(self):
        return len(self.books)




