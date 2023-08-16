#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []
    for col in matrix:
        new_matrix = list(map(lambda x: x**2, col))
        my_matrix.append(new_matrix)
    return my_matrix
