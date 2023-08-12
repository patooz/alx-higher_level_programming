#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_1 = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            list_1.append(True)
        else:
            list_1.append(False)
    return list_1
