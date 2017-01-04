#!/usr/bin/env python3

def watch():
    # S: 46979
    S = int(input())

    HOUR_SECOND = 3600
    MINUTE_SECOND = 60

    h = S // HOUR_SECOND
    m = (S % HOUR_SECOND) // MINUTE_SECOND
    s = (S % HOUR_SECOND) % MINUTE_SECOND
    print('{0}:{1}:{2}'.format(h, m, s))

if __name__ == '__main__':
    watch()
