from functools import wraps

"""
Показать возможность вызова декорируемых функций через wraps
"""


def decor1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Decorator #1")
        return result

    return wrapper


def decor2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Decorator #2")
        return result

    return wrapper


@decor1
@decor2
def prefix_name(name):
    return f"Mr.(s) {name}"


if __name__ == "__main__":
    print(prefix_name("Dmytro"))
    print(prefix_name.__wrapped__("Vasyl"))
    print(prefix_name.__wrapped__.__wrapped__("Pavel"))
