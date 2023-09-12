#!/usr/bin/python3
""" defines a function that changes a class to json function """


def class_to_json(obj):
    """ returns  arepresantaion of data structure """
    return obj.__dict__
