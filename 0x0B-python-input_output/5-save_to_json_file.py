#!/usr/bin/python3
""" defines a function that writes to a file """
import json


def save_to_json_file(my_obj, filename):
    """ writes to a file """
    with open(filename, "w") as y:
        json.dump(my_obj. y)
