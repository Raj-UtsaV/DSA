"""Canonical solution metadata.

Problem Number: 53
Problem Title: Maximum Subarray
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Divide and Conquer, Dynamic Programming
Study Tags: Kadane's Algorithm
Canonical URL: https://leetcode.com/problems/maximum-subarray/
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = best = nums[0]
        for value in nums[1:]: current = max(value, current + value); best = max(best, current)
        return best
