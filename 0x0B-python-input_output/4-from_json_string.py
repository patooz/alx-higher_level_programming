#!/usr/bin/python3
""" defines a function that changes a json to string """
import json


def from_json_string(my_str):
    """ returns a json object representation to string object """
    return json.loads(my_str)
