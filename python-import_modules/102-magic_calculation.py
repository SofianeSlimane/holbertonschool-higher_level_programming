#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        
        for i in range(4 ,6):
            c = add(c, i)
        return c
    elif not(a > b):
        return sub(a, b)
    return 
print(dis.dis(magic_calculation))
