

class Base:
    """ the base of all other classess """
    __nb_objects = 0

    def __init__(self, id=None):
        """ it initializes a Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
