#!/usr/bin/env python3


def insertion_sort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v

        print(' '.join(map(str, A)))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(' '.join(map(str, a)))
    insertion_sort(a, n)
