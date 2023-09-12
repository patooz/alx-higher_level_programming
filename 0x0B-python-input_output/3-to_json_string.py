#!/usr/bin/python3
""" defines a function that changes a string to json """
import json


def to_json_string(my_obj):
    """ retunda a json representation of the string """
    return json.dumps(my_obj)
