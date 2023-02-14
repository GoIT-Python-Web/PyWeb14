class LegacySystem:
    def execute_operation(self, value1, value2, operation):
        if operation == "add":
            return value1 + value2
        elif operation == "subtract":
            return value1 - value2
        else:
            raise ValueError("Unknown operation")


class NewSystem:
    def perform_operation(self, operator, value1, value2):
        if operator == "+":
            return value1 + value2
        elif operator == "-":
            return value1 - value2
        else:
            raise ValueError("Unknown operator")


class Adapter:
    def __init__(self, adapter_):
        self.adapter = adapter_

    def perform_operation(self, operator, value1, value2):
        if operator == "+":
            return self.adapter.execute_operation(value1, value2, "add")
        elif operator == "-":
            return self.adapter.execute_operation(value1, value2, "subtract")
        else:
            raise ValueError("Unknown operator")


if __name__ == "__main__":
    legacy_system = LegacySystem()
    new_system = NewSystem()

    # Use the adapter to call the LegacySystem
    adapter = Adapter(legacy_system)
    result = adapter.perform_operation("+", 1, 2)
    print("Result from LegacySystem (via adapter):", result)

    # Use the NewSystem directly
    result = new_system.perform_operation("-", 1, 2)
    print("Result from NewSystem:", result)
