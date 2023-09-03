#!/usr/bin/python3
""" Matrix division """


def matrix_divided(matrix, div):
    """ divides the contents of a matrix """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(m_r, list) for m_r in matrix) or
            not all((isinstance(my_el, int) or isinstance(my_el, float))
                    for my_el in [num for m_r in matrix for num in m_r])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(m_r) == len(matrix[0]) for m_r in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), m_r)) for m_r in matrix])
