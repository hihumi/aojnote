#!/usr/bin/env python3

def sorting_three_numbers():
    num_list = list(map(int, input().split()))

    res = sorted(num_list)
    print('{0} {1} {2}'.format(res[0], res[1], res[2]))

    # Presentation Error:
    #for i in res:
    #   print('{} '.format(i), end = '')
        #print(i, '', end = '')
    #print()
    # for i in res:
    #    print(i, '', end = '')
    #
    #[print(i, '') for i in res]
    #[print('{} '.format(i), end = '') for i in res]
    #print()

if __name__ == '__main__':
    sorting_three_numbers()
