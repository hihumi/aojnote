#!/usr/bin/env python3


import math


def prime_numbers(x):
    if x == 2:
        return True
    if x < 2:
        return False
    if x % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 2

    return True

if __name__ == '__main__':
    n1 = int(input())
    n2 = [int(input()) for _ in range(n1)]
    print([prime_numbers(n3) for n3 in n2].count(True))
