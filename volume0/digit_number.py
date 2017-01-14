#!/usr/bin_env python3


import sys


def digit_number():
    line = sys.stdin.readlines()
    for i in line:
        a, b = map(int, i.split())
        print(len(str(a + b)))

if __name__ == '__main__':
    digit_number()
