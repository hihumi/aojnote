#!/usr/bin/env python3

def swapping_two_numbers():
    while True:
        x, y = map(int, input().split())

        if x == 0 and y == 0:
            break
        elif x < y:
            print('{0} {1}'.format(x, y))
        else:
            print('{0} {1}'.format(y, x))

if __name__ == '__main__':
    swapping_two_numbers()
