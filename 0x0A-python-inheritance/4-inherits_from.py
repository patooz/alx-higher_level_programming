#!/usr/bin/python3
""" defines an inhetited class check function """


def inherits_from(obj, a_class):
    """ checks if an object is an inherited instance of a class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
