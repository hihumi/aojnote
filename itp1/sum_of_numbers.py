#!/usr/bin/env python3


def sum_of_numbers():
    while True:
        x_l = [int(x) for x in input()]

        # or
        #
        # x_l = []
        # for x in input():
        #     x_l.append(int(x))

        if len(x_l) and x_l[0] == 0:
            break
        print(sum(x_l))

if __name__ == '__main__':
    sum_of_numbers()
