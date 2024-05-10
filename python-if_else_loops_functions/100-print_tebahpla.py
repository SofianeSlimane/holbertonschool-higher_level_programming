#!/usr/bin/python3
i = 122
j = 89

while j >= 65:
    print("{}".format(chr(i)), end="")
    print("{}".format(chr(j)), end="")
    j -= 2
    i -= 2
