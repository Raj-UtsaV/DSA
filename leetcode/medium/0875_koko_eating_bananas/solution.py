"""Canonical solution metadata.

Problem Number: 875
Problem Title: Koko Eating Bananas
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Binary Search
Study Tags: Binary Search on Answer
Canonical URL: https://leetcode.com/problems/koko-eating-bananas/
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            speed = (left + right) // 2
            if sum((pile + speed - 1) // speed for pile in piles) <= h: right = speed
            else: left = speed + 1
        return left
