class Book:
    def __init__(self, title, author, price, owner=None):
        self.title = title
        self.author = author
        self.price = price
        self.owner = owner  # User who owns the book
        self.is_lent = False
        self.lent_to = None  # User the book is lent to, if any

    def apply_discount(self, discount):
        self.price = round(self.price * (1 - discount), 2)

    def __str__(self):
        status = f" - Owned by {self.owner.name}" if self.owner else ""
        if self.is_lent and self.lent_to:
            status += f" (Lent to {self.lent_to.name})"
        return f"{self.title} by {self.author}, Price: ${self.price}{status}"


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.owned_books = []  # List of books owned by the user
    def add_book(self, book):
        self.owned_books.append(book)

    def __str__(self):
        return f"{self.name} ({self.email})"
