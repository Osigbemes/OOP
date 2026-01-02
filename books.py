import uuid
from datetime import date


class Book:
    """
    Represents a single book in the library system.
    """

    def __init__(self, title, author, year, publisher, total_copies, publication_date):
        """
        Constructor to create a new book record.
        """

        try:
            self.book_id = str(uuid.uuid4())  # Randomly generated book ID
            self.set_title(title)
            self.set_author(author)
            self.set_year(year)
            self.set_publisher(publisher)
            self.set_total_copies(total_copies)
            self.available_copies = self.total_copies
            self.set_publication_date(publication_date)

        except Exception as e:
            raise ValueError(f"Error creating book: {e}")

    # ---------------- SETTER METHODS ----------------

    def set_title(self, title) -> str:
        if not title:
            raise ValueError("Title cannot be empty")
        self.title = title

    def set_author(self, author):
        if not author:
            raise ValueError("Author cannot be empty")
        self.author = author

    def set_year(self, year):
        year = int(year)
        if year < 0:
            raise ValueError("Year must be positive")
        self.year = year

    def set_publisher(self, publisher):
        if not publisher:
            raise ValueError("Publisher cannot be empty")
        self.publisher = publisher

    def set_total_copies(self, copies):
        copies = int(copies)
        if copies < 0:
            raise ValueError("Number of copies cannot be negative")
        self.total_copies = copies

    def set_available_copies(self, copies):
        copies = int(copies)
        if copies < 0 or copies > self.total_copies:
            raise ValueError("Invalid number of available copies")
        self.available_copies = copies

    def set_publication_date(self, publication_date):
        if not isinstance(publication_date, date):
            raise TypeError("Publication date must be a date object")
        self.publication_date = publication_date

    # ---------------- GETTER METHODS ----------------

    def get_book_id(self):
        return self.book_id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_total_copies(self):
        return self.total_copies

    def get_available_copies(self):
        return self.available_copies

    def get_publication_date(self):
        return self.publication_date
