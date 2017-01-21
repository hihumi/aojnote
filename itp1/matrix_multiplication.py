#!/usr/bin/env python3


def matrix_multiplication():
    n, m ,l = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    B = [list(map(int, input().split())) for _ in range(m)]
    C = [[sum(Ak * Bk for Ak, Bk in zip(Ai, Bj)) for Bj in zip(*B)] for Ai in A]

    for ci in C:
        print(*ci)

if __name__ == '__main__':
    matrix_multiplication()
