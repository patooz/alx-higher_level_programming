#!/usr/bin/python3
""" defines class MyInt """


class MyInt(int):
    """ manipulates the operators """

    def __eq__(self, value):
        """ changes == to != """
        return self.real != value

    def __ne__(self, value):
        """ changes != to == """
        return self.real == value
