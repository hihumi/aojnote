#!/usr/bin/env python3


def spreadsheet():
        r, c = list(map(int, input().split()))

        all_l = []
        for i in range(r):
            row = [int(i) for i in input().split()]
            row.append(sum(row))
            print(*row)
            all_l.append(row)

        last_l = []
        for i in range(c + 1):
            print('i: ', i)
            total = 0
            for j in all_l:
                print('j[i]: ', [i], j[i])
                total += j[i]
            last_l.append(total)
        print(*last_l)

if __name__ == '__main__':
    spreadsheet()
