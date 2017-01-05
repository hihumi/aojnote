#!/usr/bin/env python3

def print_a_frame():
    hash_str = '#'
    dot_str = '.'

    while True:
        H, W = map(int, input().split())

        if H == 0 and W == 0:
            break

        print(hash_str * W)
        for i in range(1, H - 1):
            print(hash_str + (dot_str * (W - 2)) + hash_str)
        print(hash_str * W)
        print()

if __name__ == '__main__':
    print_a_frame()
