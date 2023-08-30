#!/usr/bin/python3
""" square class difinition """


class Square:
    """square class representation """

    def __init__(self, size=0):
        """ initialization of the new square """
        self.size = size

    @property
    def size(self):
        """ sets the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current size of the square """
        return (self.__size * self.__size)

    def __greaterthan__(self, val):
        """ defines the > comparator """
        return self.area() > val.area()

    def __lessthan__(self, val):
        """ defines the < comparator """
        return self.area() < val.area()

    def __greaterequal__(self, val):
        """ defines the >= comparator """
        return self.area() >= val.area()

    def __lessequal__(self, val):
        """ definea the <= comparator """
        return self.area() <= val.area()

    def __equal__(self, val):
        """ defines the == comparator """
        return self.area() == val.area()

    def __notequal__(self, val):
        """ defines the != comparator """
        return self.area() != val.area()
