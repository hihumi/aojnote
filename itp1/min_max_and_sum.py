#!/usr/bin/env python3


def min_max_and_sum():
    n1 = int(input())
    n2 = list(map(int, (input().split())))

    res_min = min(n2)
    res_max = max(n2)
    res_sum = sum(n2)
    print('{0} {1} {2}'.format(res_min, res_max, res_sum))

if __name__ == '__main__':
    min_max_and_sum()
