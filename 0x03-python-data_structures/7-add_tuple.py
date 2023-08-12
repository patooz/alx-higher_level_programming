#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_c = ()
    tup_aa = tuple_a + (0, 0)
    tup_bb = tuple_b + (0, 0)
    tup_c = tup_aa[0] + tup_bb[0], tup_aa[1] + tup_bb[1]
    return tup_c
