"""Canonical solution metadata.

Problem Number: 1011
Problem Title: Capacity To Ship Packages Within D Days
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Binary Search
Study Tags: Binary Search on Answer
Canonical URL: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def feasible(cap):
            used, load = 1, 0
            for weight in weights:
                if load + weight > cap: used += 1; load = 0
                load += weight
            return used <= days
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if feasible(mid): right = mid
            else: left = mid + 1
        return left
