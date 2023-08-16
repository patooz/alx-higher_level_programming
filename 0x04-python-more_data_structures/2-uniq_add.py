#!/usr/bin/python3
def uniq_add(my_list=[]):
    brand_list = []
    sum = 0
    for i in my_list:
        if i not in brand_list:
            sum += i
            brand_list.append(i)
    return i
