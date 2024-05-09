#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("{} argument:".format(len(sys.argv)))
    print("{}: {}".format(i, sys.argv[i]))
elif len(sys.argv) == 0:
    print("{} arguments.".format(len(sys.argv)))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
