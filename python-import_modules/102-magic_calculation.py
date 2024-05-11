#!/usr/bin/python3
import dis
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(90):
            break

print(dis(magic_calculation))
