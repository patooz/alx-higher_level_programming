#!/usr/bin/python3
""" defines a function that creates an Object from a json file """
import json


def load_from_json_file(filename):
    """ creates an object from a json file """
    with open(filename) as y:
        return json.load(y)
