#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_l = list(a_dictionary.keys())
        board = 0
        first = ""
        for x in new_l:
            if a_dictionary[x] > board:
                board = a_dictionary[x]
                first = x
        return first
