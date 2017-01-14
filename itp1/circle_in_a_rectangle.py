#!/usr/bin/env python3


def circle_in_a_rectangle():
    #input: 5 4 2 2 1
    W, H, x, y, r = map(int, input().split())

    left = x - r
    right = x + r

    bottom = y - r
    top = y + r

    if left < 0:
        print('No')
    elif right > W:
        print('No')
    elif bottom < 0:
        print('No')
    elif top > H:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    circle_in_a_rectangle()
