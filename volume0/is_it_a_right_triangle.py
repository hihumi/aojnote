#!/usr/bin/env python3


def is_it_a_right_triangle():
    n = int(input())

    for i in range(n):
        x = list(map(int, input().split()))

        stack = []
        for i in x:
            stack.append(i)
        stack.sort()

        if (stack[0]**2) + (stack[1]**2) == stack[2]**2:
            print('YES')
        else:
            print('NO')

    # or
    # for i in range(n):
    #     a, b, c = map(int, input().split())
    #     if (a*a) + (b*b) == (c*c) or (a*a) + (c*c) == (b*b) or (b*b) + (c*c) == (a*a):
    #         print('YES')
    #     else:
    #         print('NO')

if __name__ == '__main__':
    is_it_a_right_triangle()
