"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Minimum Coins
Platform: Other
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Coin Change DP
Canonical URL: Unresolved
"""

def minimum_coins(coins, amount):
    best = [0] + [amount + 1] * amount
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                best[value] = min(best[value], 1 + best[value - coin])
    return -1 if best[amount] > amount else best[amount]
