class Dog:
    def __init__(self, name):
        self._name = name
        self._sound = "Woof!"

    def speak(self):
        return self._sound


class Cat:
    def __init__(self, name):
        self._name = name
        self._sound = "Meow!"

    def speak(self):
        return self._sound


def get_pet(pet="dog"):
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


if __name__ == '__main__':

    d = get_pet("dog")
    print(d.speak())

    c = get_pet("cat")
    print(c.speak())
