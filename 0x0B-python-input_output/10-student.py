#!/usr/bin/python3
""" defines a Student class """


class Student:
    """ represents the student """

    def __init__(self, first_name, last_name, age):
        """ initializes a new Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary representation of Student """
        if (type(attrs) == list
                and all(type(x) == str for x in attrs)):
            return {y: getattr(self, y) for y in attrs if hasattr(self, y)}
        return self.__dict__
