#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    items = list(a_dictionary.items())
    items.sort()
    for item in items:
        print("{}: {}".format(item, a_dictionary[item]))
