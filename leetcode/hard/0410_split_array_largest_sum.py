"""Canonical solution metadata.

Problem Number: 410
Problem Title: Split Array Largest Sum
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum
Study Tags: Binary Search on Answer
Canonical URL: https://leetcode.com/problems/split-array-largest-sum/
"""

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def groups(limit):
            count, total = 1, 0
            for value in nums:
                if total + value > limit: count += 1; total = 0
                total += value
            return count
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if groups(mid) <= k: right = mid
            else: left = mid + 1
        return left
