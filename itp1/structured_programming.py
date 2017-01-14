#!/usr/bin/env python3


def structured_programming():
    x = int(input())

    counter = 1
    while x >= counter:
        if counter % 3 == 0 or '3' in str(counter):
            print(' {}'.format(counter), end = '')
        counter += 1
    print()

if __name__ == '__main__':
    structured_programming()
