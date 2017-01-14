#!/usr/bin/env python3


def finding_missing_cards():
    deck_l = [
        '{0} {1}'.format(suit, rank)
        for suit in ('S', 'H', 'C', 'D')
        for rank in range(1, 14)
    ]

    n = int(input())
    for _ in range(n):
        S_H_C_D_and_rank = input()
        deck_l.remove(S_H_C_D_and_rank)

    for x in deck_l:
        print(x)

if __name__ == '__main__':
    finding_missing_cards()
