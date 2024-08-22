#!/usr/bin/python3
'''
    Change making module.
'''


def makeChange(coins, total):
    '''
        Determines the fewest number of coins needed to meet a given
        amount total.
        -   when given a pile of coins of different values.
    '''
    if total <= 0:
        return 0
    remainder = total
    coinsCount = 0
    coinIdx = 0
    sortedCoins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coinIdx >= n:
            return -1
        if remainder - sortedCoins[coin_idx] >= 0:
            remainder -= sortedCoins[coin_idx]
            coinsCount += 1
        else:
            coinIdx += 1
    return coinsCount
