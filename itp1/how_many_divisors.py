#!/usr/bin/env python3

def how_many_divisors():
    a, b, c = map(int, input().split())

    counter = 0
    for i in range(a, b + 1):
        if c % i == 0:
            counter += 1
    print(counter)

if __name__ == '__main__':
    how_many_divisors()
