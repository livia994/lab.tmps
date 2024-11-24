Lab_3_TMPS: Behavioral Design Patterns
----------------------------------------
### Author: Gîncu Olivia

### Objectives:
1. Study and understand the Behavioral Design Patterns.
2. As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.
3. Implement some additional functionalities using behavioral design patterns.
### Domain:
For this project, I have continued my library system created for Lab 1 and 2. The system manages books, authors, genres and allows users to add, delete, lend a book, list books in library and also a user can input the price of a book in his library and add a discount to it in form of (0.20 as 20%). This lab improves the previous version by implementing behavioral design patterns to better manage communication and interactions between system components.

### Used Design Patterns:
1. Observer: Implements a notification system that observes and notifies users of changes, such as when a new user is registered or a book is added or deleted.
2. Command: Encapsulates actions (such as user registration, adding books, etc.) into command objects, enabling easy undo/redo functionality.

### Implementation:
For this project I have used Python which follows object-oriented principles to integrate 2 behavioral design patterns in a library management system.

### 1. Observer Pattern:
- Is used to notify users of system changes.
- When any action is taken as an user is registered or a books is added or removed, a notification to all registered users is sent. 
- A "UserNotificationObserver" is attached to each user of the system, and whenever changes occur, the observer triggers notifications for that user.
### Code snippet:
```
class UserNotificationObserver(Observer):
    def __init__(self, user):
        self.user = user

    def update(self, message):
        print(f"[Notification to {self.user.name}] {message}")
```
### Purpose: 
To enable real-time notifications to users, when any change occur to the library system, keeping users informed.

### 2. Command Pattern:
- The Command Pattern encapsulates users actions into command objects, to store in a history list actions as user registration, adding or deleting books.
- Also allows for undo/redo, by reversing or undoing the last command based on user input.
- Undo/Redo works by saving user actions into a history stack, by reapllying the command when needed.
### Code Snippet:
```
class Library:
    def __init__(self):
        self.history = []

    def add_user(self, user):
        self.users.append(user)
        self.history.append(('add_user', user))  

```
### Purpose:
The Command Patterns enables the ability to do undo/redo of users recent actions and also keeping track of them.
### Conclusion:
The Observer pattern enables real-time notifications and Command simplifies undo/redo functionality by encapsulating actions. These patterns improve the organization of the system, but also enhance its usability by allowing easy management of user actions and system events.

