#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_max = 0
    current_min = potential_min = prices[0]
    for price in prices[1:]:
        if price < potential_min:
            potential_min = price
        if price > current_max:
            current_max = price
            current_min = potential_min
    return current_max - current_min if current_max != current_min else 0 - potential_min


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
