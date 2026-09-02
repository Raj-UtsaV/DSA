"""Canonical solution metadata.

Problem Number: 1283
Problem Title: Find the Smallest Divisor Given a Threshold
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Binary Search
Study Tags: Binary Search on Answer
Canonical URL: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
"""

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            divisor = (left + right) // 2
            if sum((x + divisor - 1) // divisor for x in nums) <= threshold: right = divisor
            else: left = divisor + 1
        return left
