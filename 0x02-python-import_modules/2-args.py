#!/usr/bin/python3
if __name__ == "__name__":
    import sys

    name = len(sys.argv) - 1
    if name == 0:
        print("0 arguments.")
    elif name == 1:
        print("! argument:")
    else:
        print("{} arguments:".format(name))
    for i in range(name):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
