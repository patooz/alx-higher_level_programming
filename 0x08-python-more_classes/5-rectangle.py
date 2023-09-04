#!/usr/bin/python3
""" Rectangle class definition """


class Rectangle:
    """ a class that reperesents a rectangle """
    def __init__(self, width=0, height=0):
        """ new rectangle initialization """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of the triangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of the rectange """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ rectangle in a printable format """
        if self.__width == 0 or self.__height == 0:
            return ("")
        ptr = []
        for x in range(self.__height):
            [ptr.append('#') for i in range(self.width)]
            if x != self.__height - 1:
                ptr.append("\n")
        return ("".join(ptr))

    def __repr__(self):
        """ string representation of a rectangel """
        ptr = "Rectangle(" + str(self.__width)
        ptr += ", " + str(self.__height) + ")"
        return (ptr)

    def __del__(self):
        """ deletes the rectangle """
        print("Bye rectangle...")
