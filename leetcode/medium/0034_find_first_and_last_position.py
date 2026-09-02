"""Canonical solution metadata.

Problem Number: 34
Problem Title: Find First and Last Position of Element in Sorted Array
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Binary Search
Study Tags: Lower Bound, Upper Bound
Canonical URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, bisect_right(nums, target) - 1]
