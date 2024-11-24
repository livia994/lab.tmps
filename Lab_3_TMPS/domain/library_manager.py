import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lab_3_TMPS.models.models import Book, User
from Lab_3_TMPS.notifications.notifications import NotificationAdapter, ExternalNotificationService, \
    UserNotificationObserver


class LibraryFacade:
    def __init__(self):
        self.books = []
        self.users = []
        self.notification_service = NotificationAdapter(ExternalNotificationService())
        self.observers = []  # List of observers
        self.history = []  # To track actions for undo/redo functionality
        self.redo_actions = []  # Separate list for redo actions
        self.user_notifications_sent = {}  # Track if user notification was already sent

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, user):
        self.observers = [observer for observer in self.observers if
                          not isinstance(observer, UserNotificationObserver) or observer.user != user]
    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def add_user(self, name, email):
        # Check if the user already exists
        existing_user = self.find_user(name)
        if existing_user:
            print(f"[Library] User '{name}' already exists.")
            return existing_user  # Return existing user instead of adding again

        user = User(name, email)
        self.users.append(user)

        # Add observer only if the user is newly created
        observer_exists = any(isinstance(obs, UserNotificationObserver) and obs.user == user for obs in self.observers)
        if not observer_exists:
            observer = UserNotificationObserver(user)
            self.add_observer(observer)

        self.notify_observers(f"New user registered: {name}")
        print(f"[Library] User '{name}' registered.")
        self.history.append(('add_user', user))  # Save the action for undo/redo
        return user

    def validate_price(self, price_input):
        """Validates the price input and converts it to a float if valid."""
        try:
            price = float(price_input)
            if price < 0:
                raise ValueError("Price cannot be negative.")
            return price
        except ValueError:
            print("[Library] Invalid price input. Please enter a valid number.")
            return None

    def add_book_to_user(self, user_name, title, author, price_input):
        price = self.validate_price(price_input)
        if price is None:
            print("[Library] Book not added due to invalid price.")
            return

        user = self.find_user(user_name)
        if user:
            book = Book(title, author, price, owner=user)
            user.add_book(book)
            self.books.append(book)
            self.notify_observers(f"{user_name} added a new book '{title}' by {author}.")
            print(f"[Library] Book '{title}' added to {user_name}'s library.")
            self.history.append(('add_book_to_user', user_name, book))  # Save the action for undo/redo
        else:
            print(f"[Library] User '{user_name}' not found. Register first to add books.")

    def lend_book(self, lender_name, borrower_name, book_title):
        lender = self.find_user(lender_name)
        borrower = self.find_user(borrower_name)
        book = next((b for b in lender.owned_books if b.title == book_title and not b.is_lent), None)

        if lender and borrower and book:
            book.is_lent = True
            book.lent_to = borrower
            self.notify_observers(f"{lender_name} lent the book '{book_title}' to {borrower_name}.")
            print(f"[Library] Book '{book_title}' lent to {borrower_name}.")
            self.history.append(('lend_book', lender_name, borrower_name, book))  # Save the action for undo/redo
        else:
            self.notify_observers(f"Failed to lend '{book_title}' from {lender_name} to {borrower_name}.")
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
                self.history.append(('delete_book_from_user', user, book))  # Save the action for undo/redo
            else:
                self.notification_service.notify_user(user, f"Book '{book_title}' not found in your library.")
                print(f"Book '{book_title}' not found in {name}'s library.")
        else:
            self.notification_service.notify_user(None, f"User '{name}' not found.")
            print(f"User '{name}' not found.")

    def undo_last_action(self):
        if self.history:
            action = self.history.pop()
            self.redo_actions.append(action)
            # Undo logic based on the action type
            if action[0] == 'add_user':
                user = action[1]
                self.remove_user(user.name)
            elif action[0] == 'add_book_to_user':
                user_name = action[1]
                book = action[2]
                user = self.find_user(user_name)
                if user:
                    user.remove_book(book)
                    self.books.remove(book)
            elif action[0] == 'remove_user':
                user = action[1]
                self.add_user(user.name, user.email)

    def redo_last_action(self):
        if not self.history:
            print("[Library] No actions to redo.")
            return

        last_action = self.history[-1]
        action_type = last_action[0]

        if action_type == 'add_user':
            user = last_action[1]
            if user not in self.users:
                self.add_user(user.name, user.email)
                self.add_observer(UserNotificationObserver(user))  # Add observer when redoing
        elif action_type == 'remove_user':
            user = last_action[1]
            if user in self.users:
                self.remove_user(user.name)

    def remove_user(self, name):
        user = self.find_user(name)
        if user:
            self.users.remove(user)
            # Remove the observer for the user
            self.remove_observer(user)
            self.notify_observers(f"User '{name}' removed.")
            print(f"[Library] User '{name}' removed.")
            self.history.append(('remove_user', user))  # Save the action for undo/redo
        else:
            print(f"[Library] User '{name}' not found.")

    def return_book(self, lender_name, borrower_name, book_title):
        lender = self.find_user(lender_name)
        borrower = self.find_user(borrower_name)
        if lender and borrower:
            book = next((b for b in self.books if b.title == book_title and b.lent_to == borrower), None)
            if book:
                book.is_lent = False
                book.lent_to = None
                print(f"[Library] Book '{book_title}' returned to {lender_name}.")
            else:
                print("[Library] Book not found or not lent.")
