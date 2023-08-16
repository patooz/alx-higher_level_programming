#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    brand_item = {}
    for key, value in a_dictionary.items():
        brand_item.update({ke: (value * 2)})
    return brand_item
