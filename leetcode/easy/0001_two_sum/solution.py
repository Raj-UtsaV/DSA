"""Canonical solution metadata.

Problem Number: 1
Problem Title: Two Sum
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Hash Table
Study Tags: Complement Lookup
Canonical URL: https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for index, value in enumerate(nums):
            if target - value in seen: return [seen[target-value], index]
            seen[value] = index
        return []
