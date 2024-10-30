import unittest
from Lab_1_TMPS.models.book_builder import BookBuilder
from Lab_1_TMPS.domain.book import Book, Author, Genre

class TestBookBuilder(unittest.TestCase):

    def test_book_builder(self):
        builder = BookBuilder()
        book = (builder.set_title("Test Title")
                        .set_author("Test Author", "Test Bio")
                        .set_genre("Fiction")
                        .set_id("12345")
                        .build())

        self.assertEqual(book.title, "Test Title")
        self.assertEqual(book.author.name, "Test Author")
        self.assertEqual(book.genre.name, "Fiction")
        self.assertEqual(book.id, "12345")

if __name__ == '__main__':
    unittest.main()
