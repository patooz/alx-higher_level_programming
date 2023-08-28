#!/usr/bin/python3
def magic_calculation(a, b):
    m = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            m += a ** b / i
        except Exception:
            m = b + a
            break
    return m
