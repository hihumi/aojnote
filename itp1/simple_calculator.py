#!/usr/bin/env python3


def simple_calculator():
    while True:
        a, op, b = input().split()

        a = int(a)
        b = int(b)

        if op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        elif op == '*':
            print(a * b)
        elif op == '/':
            print(a // b)
        else:
            break

if __name__ == '__main__':
    simple_calculator()
