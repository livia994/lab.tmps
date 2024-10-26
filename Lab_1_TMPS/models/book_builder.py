from Lab_1_TMPS.domain.book import Book, Author, Genre

class BookBuilder:
    def __init__(self):
        self.title = None
        self.author = None
        self.genre = None
        self.id = None

    def set_title(self, title):
        self.title = title
        return self

    def set_author(self, name, bio=""):
        self.author = Author(name, bio)
        return self

    def set_genre(self, genre_name):
        self.genre = Genre(genre_name)
        return self

    def set_id(self, id):
        self.id = id
        return self

    def build(self):
        return Book(self.title, self.author, self.genre, self.id)
