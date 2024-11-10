import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lab_2_TMPS.models.models import Book, User
from Lab_2_TMPS.notifications.notifications import NotificationAdapter, ExternalNotificationService


class LibraryFacade:
    def __init__(self):
        self.books = []
        self.users = []
        self.notification_service = NotificationAdapter(ExternalNotificationService())  # Using the updated service

    def add_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        print(f"[Library] User '{name}' registered.")
        return user

    def add_book_to_user(self, user_name, title, author, price):
        user = self.find_user(user_name)
        if user:
            book = Book(title, author, price, owner=user)
            user.add_book(book)
            self.books.append(book)
            print(f"[Library] Book '{title}' added to {user_name}'s library.")
        else:
            print(f"[Library] User '{user_name}' not found. Register first to add books.")

    def validate_price(self, input_value):
        try:
            return float(input_value)
        except ValueError:
            print("Invalid format: Price should be a decimal number. Try again.")
            return None

    def lend_book(self, lender_name, borrower_name, book_title):
        lender = self.find_user(lender_name)
        borrower = self.find_user(borrower_name)
        book = next((b for b in lender.owned_books if b.title == book_title and not b.is_lent), None)

        if lender and borrower and book:
            book.is_lent = True
            book.lent_to = borrower
            self.notification_service.notify_user(borrower, f"{lender_name} has lent {borrower_name} '{book_title}'.")
            print(f"[Library] Book '{book_title}' lent to {borrower_name}.")
        else:
            self.notification_service.notify_user(lender, f"Failed to lend '{book_title}' to {borrower_name}. Either the book is already lent or users were not found.")
            print("[Library] Lender, borrower, or available book not found.")

    def find_user(self, name):
        return next((u for u in self.users if u.name == name), None)

    def get_all_users(self):
        return self.users

    def get_all_books(self):
        return self.books

    def get_discounted_book(self, title, discount):
        book = next((b for b in self.books if b.title == title), None)
        if book:
            book.apply_discount(discount)
            return book
        else:
            self.notification_service.notify_user(None, f"Book '{title}' not found.")
            print("[Library] Book not found.")
            return None

    def delete_book_from_user(self, name, book_title):
        """Deletes a book from a user's library and from the global book list."""
        user = next((u for u in self.users if u.name == name), None)
        if user:
            # Find the book by title and remove it from the user's owned_books
            book = next((b for b in user.owned_books if b.title == book_title), None)
            if book:
                # Remove the book from the user's library (owned_books)
                user.owned_books.remove(book)
                self.books.remove(book)  # Remove the book from the global list
                self.notification_service.notify_user(user, f"Book '{book_title}' has been deleted from your library.")
                print(f"Book '{book_title}' has been deleted from {name}'s library.")
            else:
                self.notification_service.notify_user(user, f"Book '{book_title}' not found in your library.")
                print(f"Book '{book_title}' not found in {name}'s library.")
        else:
            self.notification_service.notify_user(None, f"User '{name}' not found.")
            print(f"User '{name}' not found.")