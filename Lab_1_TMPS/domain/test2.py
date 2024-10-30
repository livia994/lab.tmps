import unittest
from Lab_1_TMPS.domain.library import Library
from Lab_1_TMPS.domain.book import Book, Author, Genre

class TestLibrary(unittest.TestCase):

    def setUp(self):
        Library._instance = None  # This resets the singleton instance
        self.library = Library()
        self.book1 = Book("Book One", Author("Author One"), Genre("Fiction"), "12345")
        self.book2 = Book("Book Two", Author("Author Two"), Genre("Non-Fiction"), "67890")

    def test_singleton_library(self):
        library2 = Library()
        self.assertIs(library2, self.library)

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.assertIn(self.book1, self.library.list_books())
        self.assertIn(self.book2, self.library.list_books())

    def test_list_books(self):
        self.library.add_book(self.book1)
        self.assertEqual(len(self.library.list_books()), 1)
        self.library.add_book(self.book2)
        self.assertEqual(len(self.library.list_books()), 2)  # Update to check for 2 books

if __name__ == '__main__':
    unittest.main()
