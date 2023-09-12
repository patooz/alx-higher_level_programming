#!/usr/bin/python3
""" adds attributes to objects """


def _attribute(i, j, value):
    """ adds a new attribute to the object """
    if not hasattr(i, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(i, j, value)
