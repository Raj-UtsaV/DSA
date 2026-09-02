"""Canonical solution metadata.

Problem Number: 75
Problem Title: Sort Colors
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Two Pointers, Sorting, Quicksort, Bubble Sort
Study Tags: Dutch National Flag
Canonical URL: https://leetcode.com/problems/sort-colors/
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = mid = 0; high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0: nums[low], nums[mid] = nums[mid], nums[low]; low += 1; mid += 1
            elif nums[mid] == 1: mid += 1
            else: nums[mid], nums[high] = nums[high], nums[mid]; high -= 1
