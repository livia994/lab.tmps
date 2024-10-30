import random
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
        return f"{self.name}"


class Book:
    def __init__(self, title, author, genre, id=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.id = id if id is not None else self.generate_random_id()

    def generate_random_id(self):
        return str(random.randint(100000000, 999999999))  # Generate a random 9-digit ID

    def __str__(self):
        return f"'{self.title}' by {self.author} [Genre: {self.genre}, ID: {self.id}]"

