#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    typing = len(sys.argv) - 1
    if typing == 0:
        print("0 arguments.")
    elif typing == 1:
        print("! argument:")
    else:
        print("{} arguments:".format(typing))
    for i in range(typing):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
