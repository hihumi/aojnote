#!/usr/bin/env python3

def how_many_ways():
    while True:
        n, m = map(int, input().split())

        if n == m == 0:
            break

        counter = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if i + j + k == m:
                        counter += 1
        print(counter)

if __name__ == '__main__':
    how_many_ways()
