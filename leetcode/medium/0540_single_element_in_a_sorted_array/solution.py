"""Canonical solution metadata.

Problem Number: 540
Problem Title: Single Element in a Sorted Array
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Binary Search
Study Tags: Pair-Index Parity
Canonical URL: https://leetcode.com/problems/single-element-in-a-sorted-array/
"""

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = ((left + right) // 2) & ~1
            if nums[mid] == nums[mid + 1]: left = mid + 2
            else: right = mid
        return nums[left]
