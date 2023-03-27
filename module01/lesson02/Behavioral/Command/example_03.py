class Operation:
    def __init__(self, value_one, value_two):
        self.value_one = value_one
        self.value_two = value_two
        self.commands = {
            'add': AddCommand(self),
            'sub': SubCommand(self)
        }

    def add(self):
        return self.value_one + self.value_two

    def sub(self):
        return self.value_one - self.value_two

    def execute(self, command_name):
        return self.commands[command_name].execute()


class AddCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.add()


class SubCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.sub()


if __name__ == '__main__':
    op = Operation(10, 5)
    r = op.execute('add')
    print(r)
    r = op.execute('sub')
    print(r)
