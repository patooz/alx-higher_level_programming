#!/usr/bin/python3
""" defines a function that reads a file """


def read_file(filename=""):
    """ prints the contents of a file """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
