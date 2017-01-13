#!/usr/bin/env python3

def qq():
    [print('{0}x{1}={2}'.format(i, j, i * j)) for i in range(1, 9 + 1) for j in range(1, 9 + 1)]

if __name__ == '__main__':
    qq()
