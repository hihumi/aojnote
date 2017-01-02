#!/usr/bin/env python3

def small_large_or_equal():
    a, b = map(int, input().split())

    if a < b:
        print('a < b')
    elif a > b:
        print('a > b')
    else:
        print('a == b')

small_large_or_equal()
