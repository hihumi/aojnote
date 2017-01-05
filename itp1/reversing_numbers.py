#!/usr/bin/env python3

def reversing_numbers():
    n1 = int(input())
    n2 = list(map(int, input().split()))


    n2.reverse()
    print(*n2)

    #
    # or
    #
    # print(*reversed(n2))
    #

if __name__ == '__main__':
    reversing_numbers()
