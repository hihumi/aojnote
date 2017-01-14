#!/usr/bin/env python3


def matrix_vector_multiplication():
    n, m = map(int, input().split())

    mat_A = []
    for i in range(n):
        mat_A.append(list(map(int, input().split())))

    vec_b = []
    for i in range(m):
        vec_b.append(int(input()))

    for i in range(n):
        vec_c_i = 0
        for j in range(m):
            vec_c_i += (mat_A[i][j] * vec_b[j])
        print(vec_c_i)

if __name__ == '__main__':
    matrix_vector_multiplication()
