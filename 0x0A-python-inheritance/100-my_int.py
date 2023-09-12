#!/usr/bin/python3
""" defines class MyInt """


class MyInt(int):
    """ manipulates the operators """

    def __equalsto__(self, value):
        """ changes == to != """
        return self.real != value

    def __notequalto__(self, value):
        """ changes != to == """
        return self.real == value
