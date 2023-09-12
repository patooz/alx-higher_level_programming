#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers representing pascals triangle """
    if n <= 0:
        return []
    i = [[1]]
    while len(i) != n:
        j = i[-1]
        k = [1]
        for x in range(len(j) - 1):
            k.append(j[x] + j[x + 1])
        k.append(1)
        i.append(k)
    return i
