#!/usr/bin/python3
""" adds attributes to objects """


def _attribute(obj, att, value):
    """ adds a new attribute to the object """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
