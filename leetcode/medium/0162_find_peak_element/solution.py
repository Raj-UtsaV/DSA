"""Canonical solution metadata.

Problem Number: 162
Problem Title: Find Peak Element
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Binary Search
Study Tags: Slope Binary Search
Canonical URL: https://leetcode.com/problems/find-peak-element/
"""

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]: left = mid + 1
            else: right = mid
        return left
