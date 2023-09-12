#!/usr/bin/python3
""" defines a function that inserts text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a text after each line """
    cont = ""
    with open(filename) as x:
        for space in x:
            cont += space
            if search_string in space:
                cont += new_string
    with open(filename, "w") as y:
        y.write(cont)
