#!/usr/bin/python3
""" defins s function that appends a string to a file """


def append_write(filename="", text=""):
    """ appends a string to a file """
    with open(filename, "a", encoding="utf-8") as y:
        return y.write(text)
