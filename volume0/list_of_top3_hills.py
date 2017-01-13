#!/usr/bin/env python3

def list_of_top3_hills():
    stack1 = []
    for i in range(10):
        heights_of_ten_mountains = list(int(i) for i in input().split())
        stack1.append(heights_of_ten_mountains)

    stack1.sort(reverse = True)

    for i in range(3):
        print(*stack1[i])

if __name__ == '__main__':
    list_of_top3_hills()
