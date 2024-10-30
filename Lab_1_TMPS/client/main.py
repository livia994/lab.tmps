import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lab_1_TMPS.domain.library import Library
from Lab_1_TMPS.models.book_builder import BookBuilder
from Lab_1_TMPS.factory.genre_factory import GenreFactory


def main():
    library = Library()  # Singleton instance of Library

    while True:
        print("\nWelcome to the Library!")
        print("1. Add a Book")
        print("2. Delete a Book")
        print("3. List Books")
        print("4. Exit")

        choice = input("Please choose an option (1-4): ")

        if choice == '1':
            # Adding a book
            title = input("Enter the book title: ")
            author_name = input("Enter the author's name: ")
            author_bio = input("Enter the author's bio (optional): ")
            genre_name = input("Enter the genre: ")

            # Create a Genre using the Factory Method
            genre = GenreFactory.create_genre(genre_name)

            # Builder pattern to create a Book
            book_builder = BookBuilder()
            book = (book_builder.set_title(title)
                    .set_author(author_name, author_bio)
                    .set_genre(genre)
                    .build())  # ID is generated automatically

            library.add_book(book)
            print(f"Book '{title}' added successfully!")

        elif choice == '2':
            # Deleting a book
            book_id = input("Enter the ID of the book to delete: ")
            if library.delete_book(book_id):
                print(f"Book with ID '{book_id}' deleted successfully!")
            else:
                print(f"No book found with ID '{book_id}'.")

        elif choice == '3':
            # Listing books
            print("\nBooks in the Library:")
            for book in library.list_books():
                print(book)

        elif choice == '4':
            print("Exiting the Library. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
