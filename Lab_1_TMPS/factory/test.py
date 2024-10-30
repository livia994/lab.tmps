import unittest
from Lab_1_TMPS.factory.genre_factory import GenreFactory
from Lab_1_TMPS.domain.book import Genre

class TestGenreFactory(unittest.TestCase):

    def test_create_genre(self):
        genre = GenreFactory.create_genre("Fantasy")
        self.assertIsInstance(genre, Genre)
        self.assertEqual(genre.name, "Fantasy")

if __name__ == '__main__':
    unittest.main()
