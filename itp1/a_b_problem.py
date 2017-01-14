#!/usr/bin/env python3


def a_b_problem():
    a, b = map(int, input().split())

    d = a // b
    r = a % b
    f = a / b
    print('{0} {1} {2:f}'.format(d, r, f))

if __name__ == '__main__':
    a_b_problem()
