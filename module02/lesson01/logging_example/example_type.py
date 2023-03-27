from typing import List, Union, TypeVar, Any

Number = int | float  # Union[float, int]  #
T = TypeVar("T", int, str, float, list)


def calculator(x: T, y: T) -> T:
    return x + y


def my_mul(data: List[Number]) -> float:
    result = 1.0
    for num in data:
        result = result * num
    return result


if __name__ == "__main__":
    r = my_mul([2, 3, 4.5])
    print(r)
    print(calculator(3, 5))
    print(calculator("Hello", "World"))
    print(calculator(3.5, 4))
    print(calculator([2, 3, 4.5], [2, 3, 4.5]))
