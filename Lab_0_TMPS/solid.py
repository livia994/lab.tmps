# Book class: stores book information
class Book:
    """A class responsible for storing book information."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

# BookManager class: manages the library's collection of books
class BookManager:
    """A class responsible for managing books in the library."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a new book to the library."""
        self.books.append(book)

    def display_books(self):
        """Display available books in the library."""
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Borrowed"
            print(f"Title: {book.title}, Author: {book.author}, Status: {status}")

# BorrowPolicy classes: handle different borrowing limits (standard vs premium)
class BorrowPolicy:
    """A base class for defining borrowing policies."""
    def can_borrow(self, borrowed_count):
        raise NotImplementedError("Subclasses should implement this method.")

class StandardPolicy(BorrowPolicy):
    """A policy that allows standard users to borrow up to 2 books."""
    def can_borrow(self, borrowed_count):
        return borrowed_count < 2

class PremiumPolicy(BorrowPolicy):
    """A policy that allows premium users to borrow up to 5 books."""
    def can_borrow(self, borrowed_count):
        return borrowed_count < 5

# BorrowManager class: handles borrowing and returning books
class BorrowManager:
    """A class responsible for borrowing and returning books."""
    def __init__(self, policy):
        self.policy = policy
        self.borrowed_books = []

    def borrow_book(self, book):
        """Borrow a book if the user is allowed to borrow more books."""
        if not book.is_borrowed and self.policy.can_borrow(len(self.borrowed_books)):
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"You have borrowed '{book.title}'")
        else:
            print(f"Cannot borrow '{book.title}'.")

    def return_book(self, book):
        """Return a borrowed book."""
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"You have returned '{book.title}'")
        else:
            print(f"'{book.title}' was not borrowed.")

# Example usage of the classes

# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Add books to the library
library = BookManager()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display available books
print("Library Books:")
library.display_books()

# Borrow books with StandardPolicy
borrow_manager = BorrowManager(StandardPolicy())

# Borrow two books
borrow_manager.borrow_book(book1)
borrow_manager.borrow_book(book2)
borrow_manager.borrow_book(book3)  # This should fail due to the borrowing limit

# Display books again to see the status
print("\nAfter Borrowing:")
library.display_books()

# Return a book
borrow_manager.return_book(book1)

# Borrow the third book
borrow_manager.borrow_book(book3)

# Display books after returning and borrowing again
print("\nFinal Status:")
library.display_books()
