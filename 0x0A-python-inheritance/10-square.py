#!/usr/bin/python3
""" A rectangle class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ initializes a new square """

    def __init__(self, size):
        """ a new square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
