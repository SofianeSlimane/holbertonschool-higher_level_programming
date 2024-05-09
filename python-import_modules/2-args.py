#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        if len(sys.argv) == 1:
            print("{}: {}".format(len(sys.argv), sys.argv[1]))
            break
        elif len(sys.argv) == 0:
            print("{} arguments.".format(len(sys.argv)))
            break
        else:
            print("{}: {}".format(i, sys.argv[i]))
