#!/usr/bin/python3
""" defines a class function """


def is_same_class(obj, a_class):
    """ checks is an object is an instance of a class """
    if type(obj) == a_class:
        return True
    return False
