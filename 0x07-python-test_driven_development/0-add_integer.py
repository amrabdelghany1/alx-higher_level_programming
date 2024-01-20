#!/usr/bin/python3
""" This module to add two integers. """

def add_integers(a, b=98):
    """
    Adds two integers.

    Args:
        a: first input.
        b: second input by default 98.
    
    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        Sum of the two ints.

    """

    if type(a) not in (int, float):
        raise TypeError(" a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/0-add_integer.txt')

