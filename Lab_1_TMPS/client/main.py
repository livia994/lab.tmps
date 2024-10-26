import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lab_1_TMPS.domain.library import Library
from Lab_1_TMPS.models.book_builder import BookBuilder
from Lab_1_TMPS.factory.genre_factory import GenreFactory
def main():
    # Singleton instance of Library
    library = Library()

    # Create a Genre using the Factory Method
    fiction_genre = GenreFactory.create_genre("Fiction")

    # Use Builder to create a Book
    book_builder = BookBuilder()
    book1 = (book_builder.set_title("The Great Gatsby")
                          .set_author("F. Scott Fitzgerald", "American novelist")
                          .set_genre(fiction_genre)
                          .set_isbn("9780743273578")
                          .build())

    # Add book to the library
    library.add_book(book1)

    # Print all books in the library
    for book in library.list_books():
        print(book)

if __name__ == "__main__":
    main()
