#!/usr/bin/env python3

#Print Many Hello World
def print_many_hello_world():

    hw = 'Hello World'
    for i in range(1000):
        print(hw)

    # Presentation Error:
    # hw1000 = "Hello World\n" * 1000
    # print(hw1000)
if __name__ == '__main__':
    print_many_hello_world()
