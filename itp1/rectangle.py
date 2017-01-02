#!/usr/bin/env python3

def rectangle():
    num_list = list(map(int, input().split()))
    a = num_list[0]
    b = num_list[1]
    area = a * b
    perimater = 2 * (a + b)
    print("{0} {1}".format(area, perimater))

rectangle()
