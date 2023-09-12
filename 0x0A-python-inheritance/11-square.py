#!/usr/bin/python3
""" Square sub class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ represemts a square """

    def __init__(self, size):
        """ initalizes a new square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
