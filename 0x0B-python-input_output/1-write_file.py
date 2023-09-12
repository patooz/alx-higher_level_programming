#!/usr/bin/python3
""" defines a function that writes into a file """


def write_file(filename="", text=""):
    """ writes to a utf8 encodeing """
    with open(filename, "w", encoding="utf-8") as y:
        return y.write(text)
