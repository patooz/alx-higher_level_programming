#!/usr/bin/python3
""" defines the lookup function """


def lookup(obj):
    """ returns the list of available attributes/methods of object """
    return (dir(obj))
