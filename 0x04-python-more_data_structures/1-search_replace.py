#!/usr/bin/python3
def search_replace(my_list, search, replace):
    brand_list = []
    for item i my_list:
        if item == search:
            brand_list.append(replace)
        else:
            brand_list.append(item)
    return brand_list
