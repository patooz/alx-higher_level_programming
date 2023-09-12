#!/usr/bin/python3
""" defines a base geometry class """


class BaseGeometry:
    """ base geometry. """
    def area(self):
        """ not used """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the input value as int """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
