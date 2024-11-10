Lab_1_TMPS: Structural Design Patterns
----------------------------------------
### Author: Gîncu Olivia

### Objectives:
1. Study and understand the Structural Design Patterns.
2. As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.
3. Implement some additional functionalities using structural design patterns.
4. 
### Domain:
For this project, I have continued my library system created for Lab 1. The system manages books, authors, genres and allows users to add, delete, lend a book, list books in library and also a user can input the price of a book in his library and add a discount to it in form of (0.20 as 20%). This lab improves my first lab by implementing structural design patterns to improve how objects and classes are organized. 

### Used Design Patterns:
1. Facade: Provides a simplified interface for the user to interact with the library system, encapsulating systems as books, users, and notifications.
2. Adapter: Adds an external notification service, ensuring communication between the library system and external services.
3. Decorator: Adds additional functionality to books, such as discounts, without changing their original structure.

### Implementation:
For this project I have used Python which follows object-oriented principles to integrate 3 structural patterns in a library management system.

### 1. Facade Pattern:
- The "LibraryFacade" class provides a single entry point to handle various operations.
- Through this, users can add or delete books, see all registered users and books in the system, add a discount to a client's book and receive notifications. This pattern simplifies interactions for the client by hiding complex systems.
- In the original "Library" class, a singleton pattern is used to ensure that only one instance of Library exists. In the updated code, this singleton structure is further improved with the Facade pattern via "LibraryFacade" to achieve a simpler interface.
### Code snippet:
```
class LibraryFacade:
    def __init__(self):
        self.library = Library()
        self.notification_service = NotificationAdapter()
        # Additional subsystems can be added here

    def add_book(self, book):
        self.library.add_book(book)
        self.notification_service.send_notification(f"New book '{book.title}' added.")
```
### Purpose: 
To improve code readability, making the library system easier to use and modify.

### 2. Adapter Pattern:
- The "NotificationAdapter" class adds a notification service to the library system.
- It enables notifications to be sent from within the library system without changing the core library code when any action is done, e.g. when a user registers it triggers this notification: "[System Notification] Sara has lent Andrew 'Red Queen'.".

### Code Snippet:
```
class NotificationAdapter:
    def __init__(self):
        self.external_service = ExternalNotificationService()

    def send_notification(self, message):
        self.external_service.notify(message)
```
### Purpose:
The Adapter Pattern allows the library system to interact with external services, also making it easy for replacement or enhancement of the notification service if needed.
### 3. Decorator Pattern:
- The "BookDiscountDecorator" class extends the "Book" class to add discount functionality without modifying the "Book" class itself, a plus to the Builder Pattern.
- This decorator wraps "Book" instances, adding extra attributes (such as "discounted_price") and methods ("apply_discount"), providing flexibility in handling book prices.

### Code Snippet:

```
class BookDiscountDecorator:
    def __init__(self, book, discount):
        self.book = book
        self.discount = discount

    def get_discounted_price(self):
        return self.book.price * (1 - self.discount)
```
### Purpose:
The Decorator Pattern enables additional features to be added dynamically to book objects, improving the Open/Closed Principle.
### Conclusion:
This project provides an experience with three essential structural design patterns, Facade, Adapter, and Decorator. The Facade pattern simplifies client interaction with the system, the Adapter enables external notifications without modifying core logic, and the Decorator allows dynamic addition of functionality (like discounts) to books. This approach enhances both usability and scalability.


