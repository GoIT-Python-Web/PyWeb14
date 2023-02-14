class Document:
    def __init__(self):
        self.commands = {
            'save': SaveCommand(self),
            'open': OpenCommand(self),
        }

    def save(self):
        print('Saving')

    def open(self):
        print('Opening')

    def execute_command(self, command_name):
        self.commands[command_name].execute()


class SaveCommand:
    def __init__(self, document: Document):
        self.document = document

    def execute(self):
        self.document.save()


class OpenCommand:
    def __init__(self, document: Document):
        self.document = document

    def execute(self):
        self.document.open()


if __name__ == '__main__':
    document = Document()
    document.execute_command('save')  # Saving
    document.execute_command('open')  # Opening
