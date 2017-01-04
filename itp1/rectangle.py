#!/usr/bin/env python3

def rectangle():
    a, b = map(int, input().split())
    area = a * b
    perimater = 2 * (a + b)
    print('{0} {1}'.format(area, perimater))

if __name__ == '__main__':
    rectangle()
