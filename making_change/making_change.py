#!/usr/bin/python

import sys
# Here's a general idea: we can initialize a cache as a list (a dictionary would work fine as well) of 0s with a length equal to the amount we're looking to make change for. Each value of the list will represent the number of ways to make i cents, where i are the indices of the list. So cache[10] == 4 from our example above. Since we know there is one way to make 0 cents in change, we'll initialize cache[0] = 1 (you can seed entries for additional values as well, though you don't actually need to).

# Now that we've initialized our cache, we'll start building it up. We have an initial value in our cache, so we'll want to build up subsequent answers in terms of this initial value. So, for a given coin, we can loop through all of the higher amounts between our coin and the amount (i.e., for higher_amount in range(coin, amount + 1)). If we take the difference between the higher amount and the value of our coin, we can start building up the values in our cache.

# To go into a little more detail, let's walk through a small example. If we imagine our coin is a penny, in the first loop iteration, higher_amount is going to be 1 (since it will at first be the same value as our coin). If we take the difference between higher_amount and our coin value, we get 0. We already have a value for 0 in our cache; it's 1. So now we've just figured out 1 way to 1 cent from a penny. Add that answer to our cache.

# Next up, on the next iteration, higher_amount will now be 2. The difference between higher_amount and our coin value now is 1. Well we just figured out an answer for 1, so now we have an answer for 2. Add that to our cache.

def making_change(amount, denominations):

    cache = [0] * (amount + 1)
    cache[0] = 1
    for coin in denominations:
        for higher_amount in range(coin, amount+1):
            cache[higher_amount] += cache[higher_amount-coin]

    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
