#!/usr/bin/python3
""" defines a base geometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines a rectangle """

    def __init__(self, width, height):
        """ rectagle initialization """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
