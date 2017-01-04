#!/usr/bin/env python3

def print_a_rectangle():
    while True:
        H, W = list(map(int, input().split()))

        if H == 0 and W == 0:
            break
        else:
            for i in range(H):
                hash_str = ''
                for j in range(W):
                    hash_str += '#'
                print(hash_str)
        print()

if __name__ == '__main__':
    print_a_rectangle()
