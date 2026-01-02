from books import Book


class BookList:
    """
    Manages a collection of Book objects in the library system.
    """

    def __init__(self):
        """
        Constructor to create a new BookList object.
        """
        self.books = {}  # key = book_id, value = Book instance

    def add_book(self, book: Book):
        """
        Adds a Book object to the collection.
        """
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added")

        self.books[book.get_book_id()] = book

    def search_book(self, title=None, author=None, publisher=None, publication_date=None) -> Book:
        """
        Searches for books by title, author, publisher OR publication date.
        Returns a list of matching books.
        """

        if not any([title, author, publisher, publication_date]):
            raise ValueError("At least one search parameter must be provided")

        results = []

        for book in self.books.values():
            if (
                (title and book.get_title() == title) or
                (author and book.get_author() == author) or
                (publisher and book.get_publisher() == publisher) or
                (publication_date and book.get_publication_date() == publication_date)
            ):
                results.append(book)

        return results[0] if results else None

    def remove_book_by_title(self, title):
        """
        Removes a book from the collection using its title.
        Informs the user if multiple books share the same title.
        """

        if not title:
            raise ValueError("Title cannot be empty")

        matches = [bid for bid, book in self.books.items() if book.get_title() == title]

        if len(matches) == 0:
            raise ValueError("No book found with the given title")

        if len(matches) > 1:
            raise ValueError("Multiple books found with this title")

        del self.books[matches[0]]
        return True

    def count_books(self):
        """
        Returns the total number of books stored in the collection.
        """
        return len(self.books)
