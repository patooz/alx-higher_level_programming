class Square:
    def __init__(self, size=0):
        self.size = size

        @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(self, value):
            raise TypeError("size must be an integer")
        elif value < 0:
            raie TypeError("size must be an integer")
            self.__size = value

        def area(self):
            return(self.__size * self.__size)
