#!/usr/bin/env python3

def range():
    a, b, c = map(int, input().split())

    if a < b < c:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    range()
