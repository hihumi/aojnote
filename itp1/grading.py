#!/usr/bin/env python3


def grading():
    while True:
        m, f, r = map(int, input().split())

        point = m + f

        if m == f == r == -1:
            break
        if m == -1 or f == -1:
            print('F')
        elif point >= 80:
            print('A')
        elif point >= 65: # point >= 65 and point < 80
            print('B')
        elif point >= 50:
            print('C')
        elif point >= 30:
            if r >= 50:
                print('C')
            else:
                print('D')
        else:
            print('F')

if __name__ == '__main__':
    grading()
