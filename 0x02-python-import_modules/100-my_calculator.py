#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(argv - 1)
    op = ['+', '-', '*', '/']
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    for i in op:
        if sys.argv[2] != op[i]:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    if argc == 3:
        if sys.argv[2] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif sys.argv[2] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif sys.argv[2] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif sys.argv[2] == '/':
            print("{} / {} = {}".format(a, b, div(a / b)))

