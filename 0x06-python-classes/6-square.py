#!/usr/bin/python3

""" class square definition """


class Square:
    """square representation """

    def __init__(self, size=0, position=(0, 0)):
        """ initialization if the new square """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ sets the size of the square """
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ sets the current position of the square """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(k, int) for k in value) or
                not all(k >= 0 for k in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the current size of the square """
        return (self.__size * self.__size)

    def my_print(self):
        """" prints the # character """
        if self.__size == 0:
            print("")
            return
        [print("") for j in range(0, self.__position[1])]
        for j in range(0, self.__size):
            [print(" ", end="") for x in range(0, self.__position[0])]
            [print("#", end="") for m in range(0, self.__size)]
            print("")
