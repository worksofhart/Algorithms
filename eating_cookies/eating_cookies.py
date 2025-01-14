#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def memoize(func):
    memo = {}

    def wrapper(val):
        if val not in memo:
            memo[val] = func(val)
        return memo[val]
    return wrapper


def eating_cookies(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return eating_cookies(
            n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


eating_cookies = memoize(eating_cookies)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
