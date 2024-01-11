"""
Prompt:
Write a Python program that prints the sum of two floating point numbers, 
the difference between two integers, and the product of a floating point number and an integer. 
In each case, have the program print out the data type of the resulting answer.
"""


from random import random, randint


def print_result_and_type(f: callable, args: list[int | float], res: int | float) -> None:
    """Print the result and its data type"""

    print(f"result of {f}({args[0]}, {args[1]}) = ({res.__class__}, {res})")


def is_type(x: int | float, data_type: float | int) -> bool:
    """Make sure the class of the number matches the type expected"""

    return x.__class__ == data_type


def fsum(x: float, y: float) -> float:
    """Computes sum of two floating point numbers"""

    assert is_type(x, float) and is_type(y, float)
    return x + y


def idef(x: int, y: int) -> int:
    """Computes the difference of two integers"""

    assert is_type(x, int) and is_type(y, int)
    return x + y


def fmulti(x: float, y: int) -> float:
    """Computes the product of a floating point number and an integer"""

    assert is_type(x, float) and is_type(y, int)
    return x * y


def main():
    """Call functions and print the data type of the resulting answer"""

    inum = randint(0, 50)
    fnum = random() * randint(0, 10)

    print_result_and_type(fsum.__name__, [fnum, fnum], fsum(fnum, fnum))
    print_result_and_type(idef.__name__, [inum, inum], idef(inum, inum))
    print_result_and_type(fmulti.__name__, [fnum, inum], fmulti(fnum, inum))


# Call main program if the interpreter ran this file
if __name__ == "__main__":
    main()
