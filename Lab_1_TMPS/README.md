Lab_1_TMPS: Creational Design Patterns
----------------------------------------
### Author: Gîncu Olivia

### Objectives:
- Get familiar with the Creational Design Patterns
- Choose a specific domain for the project
- Implement at least 3 Creational Design Patterns within the chosen domain

### Domain:
For this project, I have chosen a library system. The system manages books, authors, and genres, and allows users to add, delete and list books in a library.

### Used Design Patterns:
1. Singleton: Ensures only one instance of the "library" class.
2. Factory Method: Creates "Genre" objects dynamically using a factory class.
3. Builder: Constructs "Book" objects with customizable properties such as title, author, genre, short bio and ID.

### Implementation:
For this project I have used Python which follows object-oriented principles to demonstrate 3 creational design patterns in a library management system.

### 1. Singleton Pattern:
- The "Library" class uses Singleton Pattern to ensure that only one instance of the library exists.
- This was achieved by overriding the "_new_" method. When a new "Library" object is requested, it checks if an istance already exists. If not, it creates one and stores it in the _instance class.

### Code snippet:
```
class Library:
    _instance =None
     def _new_(cls):
         if cls._instance is None:
             cls._instance = super(Library, cls)._new_(cls)
             cls._instance.books = []
         return cls._instance
```
### Purpose: 
Prevent issues related to multiple instances and ensuring consistent access to the library's data.

### 2. Builder Pattern:
- The "BookBuilder" class constructs "Book" objects step by step. Each method returns "self", allowing for method chaining.
- The builder takes care of setting attributes of the "Book" and then calls the build() method to create the "Book" instance.

### Code Snippet:
```
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

    def build(self):
        return Book(self.title, self.author, self.genre)
```
### Purpose:
Allows users to create a "Book" object step by step, without needing to understand the internal work.

### 3. Factory Method Pattern
- The "GenreFactory" class uses the Factory Method Pattern to create "Genre" instances.
- Instead of directly initiating the "Genre" class, the factory provides a method "create_genre" to handle creation.

### Code Snippet:

```
class GenreFactory:
    @staticmethod:
    def create_genre(genre_name):
        return Genre(genre_name)
```
### Purpose
The Factory Method pattern allows for abastraction in object creation. So, for creating a "Genre" changes, if for example we would like to add subtypes of genres, we could only modify the factory method instead of changing the whole code.

### Conclusion:
This project provides an experience with three essential creational design patterns, Factory Method, Builder and Singleton. Each one was implemented to solve specific object creation challenges within the library system. The Singleton Pattern ensured a single instance of the "Library" class, the Factory Method abstracts the creation of "Genre" objects, enabling future changes of the code, without affecting the rest of the code, and Builder facilitates the construction of "Book" objects, allowing for optional parameters as author's bio. This approach enhances code readability, making the code easier to extend and mantain.


