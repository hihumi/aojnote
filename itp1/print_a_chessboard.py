#!/usr/bin/env python3


def print_a_chessboard():
    hash_str = '#'
    dot_str = '.'
    hash_dot_str = '#.'
    dot_hash_str = '.#'

    while True:
        H, W = map(int, input().split())

        if H == 0 and W == 0:
            break

        for i in range(H):
            if i % 2 == 0:
                if W % 2 != 0:
                    print(hash_dot_str * (W // 2) + hash_str)
                    continue
                else:
                    print(hash_dot_str * (W // 2))
            else:
                if W % 2 != 0:
                    print(dot_hash_str * (W //2 ) + dot_str)
                    continue
                else:
                    print(dot_hash_str * (W // 2))
        print()

if __name__ == '__main__':
    print_a_chessboard()
