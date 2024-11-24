from Lab_3_TMPS.domain.command import Command
class UndoRedoManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()  # Clear redo stack on new action

    def undo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
        else:
            print("[Library] Nothing to undo.")

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.redo()
            self.undo_stack.append(command)
        else:
            print("[Library] Nothing to redo.")

class RegisterUserCommand:
    def __init__(self, library, name, email):
        self.library = library
        self.name = name
        self.email = email
        self.user = None

    def execute(self):
        self.user = self.library.add_user(self.name, self.email)

    def undo(self):
        if self.user:
            self.library.remove_user(self.name)

    def redo(self):
        if self.user:
            self.library.add_user(self.name, self.email)


class AddBookCommand(Command):
    def __init__(self, library, user_name, title, author, price):
        self.library = library
        self.user_name = user_name
        self.title = title
        self.author = author
        self.price = price

    def execute(self):
        self.library.add_book_to_user(self.user_name, self.title, self.author, self.price)

    def undo(self):
        self.library.delete_book_from_user(self.user_name, self.title)


class LendBookCommand(Command):
    def __init__(self, library, lender_name, borrower_name, book_title):
        self.library = library
        self.lender_name = lender_name
        self.borrower_name = borrower_name
        self.book_title = book_title

    def execute(self):
        self.library.lend_book(self.lender_name, self.borrower_name, self.book_title)

    def undo(self):
        self.library.return_book(self.lender_name, self.borrower_name, self.book_title)

