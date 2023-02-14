from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class PrintCommand(Command):
    def __init__(self, message: str):
        self.message = message

    def execute(self):
        print(self.message)


class HelloCommand(PrintCommand):
    def __init__(self):
        super().__init__("Hello")


class GoodbyeCommand(PrintCommand):
    def __init__(self):
        super().__init__("Goodbye")


if __name__ == '__main__':
    hello = HelloCommand()
    hello.execute()  # prints "Hello"
    goodbye = GoodbyeCommand()
    goodbye.execute()  # prints "Goodbye"
   