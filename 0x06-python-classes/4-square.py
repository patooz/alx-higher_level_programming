#!/usr/bin/python3

""" class square definition """


class Square:
    """square representation """

    def __init__(self, size=0):
        """ initialization if the new square """
        self.size = size

        @property
    def size(self):
        """ sets the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(self, value):
            raise TypeError("size must be an integer")
        elif value < 0:
            raie TypeError("size must be an integer")
            self.__size = value

        def area(self):
            """ returns the current size of the square """
            return(self.__size * self.__size)
