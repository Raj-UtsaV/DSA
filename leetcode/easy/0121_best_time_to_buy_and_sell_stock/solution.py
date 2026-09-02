"""Canonical solution metadata.

Problem Number: 121
Problem Title: Best Time to Buy and Sell Stock
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Dynamic Programming
Study Tags: Running Minimum
Canonical URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        best, minimum = 0, float("inf")
        for price in prices: minimum = min(minimum, price); best = max(best, price - minimum)
        return best
