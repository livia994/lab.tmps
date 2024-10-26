class Author:
    def __init__(self, name, bio=""):
        self.name = name
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.bio}"

class Genre:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


    def __str__(self):
        return f"Genre: {self.name}"


class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' by {self.author} [Genre: {self.genre}, ISBN: {self.isbn}]"
