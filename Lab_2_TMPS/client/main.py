import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lab_2_TMPS.domain.library_manager import LibraryFacade
library = LibraryFacade()

def display_menu():
    print("\nLibrary System Menu:")
    print("1. Register a User")
    print("2. Add a Book to User's Library")
    print("3. Lend a Book to Another User")
    print("4. View All Registered Users")
    print("5. View All Books")
    print("6. View Book with Discount")
    print("7. Delete a Book from User's Library")
    print("8. Exit")

def register_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    library.add_user(name, email)

def add_book_to_user():
    user_name = input("Enter the name of the user adding a book: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")

    price = None
    while price is None:
        price_input = input("Enter book price: ")
        price = library.validate_price(price_input)

    library.add_book_to_user(user_name, title, author, price)

def lend_book_to_user():
    lender_name = input("Enter the name of the user lending the book: ")
    borrower_name = input("Enter the name of the user borrowing the book: ")
    book_title = input("Enter the title of the book to lend: ")
    library.lend_book(lender_name, borrower_name, book_title)

def view_all_users():
    users = library.get_all_users()
    if users:
        print("\nRegistered Users:")
        for user in users:
            print(f"- {user.name} ({user.email})")
    else:
        print("No users registered.")

def view_all_books():
    books = library.get_all_books()
    if books:
        print("\nBooks in the Library:")
        for book in books:
            print(book)
    else:
        print("No books available.")

def view_discounted_book():
    book_title = input("Enter the title of the book to apply discount to: ")
    discount = None
    while discount is None:
        try:
            discount = float(input("Enter discount rate (e.g., 0.20 for 20%): "))
        except ValueError:
            print("Invalid format: Discount should be a decimal number (e.g., 0.20). Try again.")

    discounted_book = library.get_discounted_book(book_title, discount)
    if discounted_book:
        print("\nDiscounted Book:")
        print(f"Title: {discounted_book.title}")
        print(f"Author: {discounted_book.author}")
        print(f"Updated Price after {int(discount * 100)}% discount: ${discounted_book.price}")


def delete_book():
    # Ask for the name of the user whose library we will modify
    name = input("Enter the name of the user whose library you want to delete a book from: ")

    # Ask for the book title to delete
    book_title = input("Enter the title of the book you want to delete: ")

    library.delete_book_from_user(name, book_title)
def main():
    while True:
        print("\nWelcome to the Library!")
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            add_book_to_user()
        elif choice == "3":
            lend_book_to_user()
        elif choice == "4":
            view_all_users()
        elif choice == "5":
            view_all_books()
        elif choice == "6":
            view_discounted_book()
        elif choice == "7":
            delete_book()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()