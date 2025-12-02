import uuid
class Book:
    """
    Represents a single book in the library system.
    Each book has a unique ID and other descriptive attributes.
    """

    def __init__(self, title, author, year, publisher, total_copies, publication_date, book_id=None):
        try:
            self.book_id = book_id or str(uuid.uuid4())                     # Auto-generated unique ID
            self.title = title
            self.author = author
            self.year = int(year)
            self.publisher = publisher
            self.total_copies = int(total_copies)
            self.available_copies = int(total_copies)
            self.publication_date = publication_date
        except Exception as e:
            raise ValueError(f"Error creating book: {e}")

    # -------------- SETTER METHODS --------------
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author
        
    def set_quantity(self, quantity):
        self.total_copies = quantity

    def set_year(self, year):
        try:
            self.year = int(year)
        except Exception:
            raise ValueError("Year must be a number")

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_total_copies(self, copies):
        try:
            copies = int(copies)
            if copies < 0:
                raise ValueError("Copies cannot be negative")
            self.total_copies = copies
            self.available_copies = copies
        except Exception:
            raise ValueError("Copies must be a valid number")

    def set_publication_date(self, pub_date):
        self.publication_date = pub_date

    # -------------- GETTER METHODS --------------
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
    
    def get_quantity(self):
        return self.total_copies

    def get_available_copies(self):
        return self.available_copies

    def get_publication_date(self):
        return self.publication_date
    
class BorrowRecord:
    def __init__(self, record_id, user_id, book_id):
        self.record_id = record_id
        self.user_id = user_id
        self.book_id = book_id