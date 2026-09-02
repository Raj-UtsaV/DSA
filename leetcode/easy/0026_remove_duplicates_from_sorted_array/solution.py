"""Canonical solution metadata.

Problem Number: 26
Problem Title: Remove Duplicates from Sorted Array
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Two Pointers
Study Tags: In-Place Overwrite
Canonical URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 0
        for value in nums:
            if write == 0 or nums[write - 1] != value:
                nums[write] = value; write += 1
        return write
