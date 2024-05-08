#!/usr/bin/python3
def uppercase(str):
    unicode = 0
    new_str = ""
    for char in str:
        if ord(char) <= 90:
            unicode = ord(char)
            new_str += chr(unicode)
        elif ord(char) > 90:
            unicode = ord(char) - 32
            new_str += chr(unicode)
    print("{}".format(new_str))
