#!/usr/bin/python3

""" an int addition function """


def add_integer(a, b=98):
    """ returns the results of a and b """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an interger")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an interger")
    return (int(a) + int(b))
