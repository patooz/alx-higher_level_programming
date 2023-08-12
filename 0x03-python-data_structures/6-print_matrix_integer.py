#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mt_r in matrix:
        for mt_c in mt_r:
            print("{:d}".format(mt_c), end=" " if mt_c != mt_r[-1] else "")
