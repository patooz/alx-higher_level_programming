#!/usr/bin/python3
""" defines class Mylist """


class MyList(list):
    """ subclass list """
    def __init__(self):
        """ initialization of the object """
        super().__init__()

    def print_sorted(self):
        """ prints the list """
        print(sorted(self))
