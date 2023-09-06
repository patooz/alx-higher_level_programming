#!/usr/bin/python3
""" a function that prints a square """


def print_square(size):
    """ prints a square """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
