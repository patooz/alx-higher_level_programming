class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        size.__self = size
