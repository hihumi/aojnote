#!/usr/bin/env python3


def circle():
    r = float(input())

    PI = 3.141592653589

    area = r * r * PI
    circumference = (r * 2) * PI
    print('{0:f} {1:f}'.format(area, circumference))

if __name__ == '__main__':
    circle()
