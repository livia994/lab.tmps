class CommandInvoker:
    def __init__(self):
        self.history = []
        self.redo_stack = []

    def execute_command(self, command):
        self.history.append(command)
        self.redo_stack.clear()
        command.execute()

    def undo(self):
        if not self.history:
            print("[Invoker] No commands to undo.")
            return
        command = self.history.pop()
        command.undo()
        self.redo_stack.append(command)

    def redo(self):
        if not self.redo_stack:
            print("[Invoker] No commands to redo.")
            return
        command = self.redo_stack.pop()
        self.history.append(command)
        command.redo()
