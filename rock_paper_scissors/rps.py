#!/usr/bin/python

import sys


def rock_paper_scissors(n):

    def calculate_plays(plays, num):
        if len(plays) == n:
            return [plays]
        else:
            return calculate_plays(plays + ['rock'], n - 1) + calculate_plays(plays + ['paper'], n - 1) + calculate_plays(plays + ['scissors'], n - 1)

    return calculate_plays([], n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
