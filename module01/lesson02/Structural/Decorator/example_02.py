class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"


if __name__ == '__main__':
    component = ConcreteComponent()
    decoratorA = ConcreteDecoratorA(component)
    decoratorB = ConcreteDecoratorB(decoratorA)
    print(decoratorB.operation())
