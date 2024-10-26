class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
        return cls._instance

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return self.books
