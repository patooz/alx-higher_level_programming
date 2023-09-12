#!/usr/bin/python3
""" defines a base geometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines a rectangle """

    def __init__(self, width, height):
        """ initializes a new rectangle """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ print and str of representation of the rectangle """
        rep = "[" + str(self.__class__.__name__) + "] "
        rep += str(self.__width) + "/" + str(self.__height)
        return rep
