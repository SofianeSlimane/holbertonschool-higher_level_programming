#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    num1 = sys.argv[1]
    num2 = sys.argv[3]
    if num1.isdigit() == False or num2.isdigit() == False:
         print("Usage: ./100-my_calculator.py <a> <operator> <b>")
         exit(1)
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    op = sys.argv[2]
    
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    if op == "+":
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))

    elif op == "-":
        print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
    
    elif op == "*":
        print("{} * {} = {}".format(num1, num2,  mul(num1, num2)))

    elif op == "/":
        print("{} / {} = {}".format(num1, num2,  div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
