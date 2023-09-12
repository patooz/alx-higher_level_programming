#!/usr/bin/python3
""" defines a Student class """


class Student:
    """ represents the student """

    def __init__(self, first_name, last_name, age):
        """ initializes a new Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionary representation of Student """
        return self.__dict__
