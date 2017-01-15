#!/usr/bin/env python3


def greatest_common_divisor(x, y):
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y

    print('{}'.format(y))

if __name__ == '__main__':
    x, y = map(int, input().split())
    greatest_common_divisor(x, y)
