from typing import Callable, Any, List, TypeVar

T = TypeVar('T')


def my_map(func: Callable[[T], Any], lst: List[T]) -> List | None:
    """
    function activate function on elements in list
    :param func: func to activate
    :param lst: list of elements
    :return: list after activation on each element
    """
    try:
        new_list = list(map(func, lst))
        return new_list

    except TypeError as te:
        print("differance between list elements type and function variable type!")
        return None


def main():
    lst = my_map(len, ["say", "sah"])
    for x in lst:
        print(x)


if __name__ == "__main__":
    main()
