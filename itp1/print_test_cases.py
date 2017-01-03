#!/usr/bin/env python3

def print_test_cases():

    # sample input:
    # 3
    # 5
    # 11
    # 7
    # 8
    # 19

    counter = 1
    while True:
        x = int(input())
        if x == 0:
            break
        else:
            print('Case {0}: {1}'.format(counter, x))
        counter += 1

if __name__ == '__main__':
    print_test_cases()
