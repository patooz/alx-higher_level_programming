#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """ represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize a rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x cordinates """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y cordinates """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ area of the rectangle """
        return self.width * self.height

    def display(self):
        """ prints the rectagle using # """
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print('#', end="") for j in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """ updates the width  height of the rectangle """
        if args and len(args) != 0:
            i = 0
            for j in args:
                if i == 0:
                    if j is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = j
                elif i == 1:
                    self.width = j
                elif i == 2:
                    self.height = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
                i += 1

        elif kwargs and len(kwargs) != 0:
            for ln, m in kwargs.item():
                if ln == "id":
                    if m is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = m
                    elif ln == "width":
                        self.width = m
                    elif ln == "height":
                        self.height = m
                    elif ln == "x":
                        self.x = m
                    elif ln == "y":
                        self.y = m

    def to_dictionary(self):
        """ rectangle as a dictionary """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """ print and string represantion of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
