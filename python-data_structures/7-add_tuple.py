#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple3 = ()
    if len(tuple_a) < 2:
        while len(tuple_a) != 2:
            tuple_a += 0,
    if len(tuple_b) < 2:
        while len(tuple_b) != 2:
            tuple_b += 0,
    tuple3 = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    return tuple3
