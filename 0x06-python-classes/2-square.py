#!/usr/bin/python3

""" class square definition """


class Square:
    """square representation """
    
    def __init__(self, size=0):
        """ initialization if the new square """

        if not isinstance(size, int):
            raise TypError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        size.__self = size
