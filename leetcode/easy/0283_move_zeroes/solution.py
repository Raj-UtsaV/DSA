"""Canonical solution metadata.

Problem Number: 283
Problem Title: Move Zeroes
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Two Pointers
Study Tags: Stable Compaction
Canonical URL: https://leetcode.com/problems/move-zeroes/
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0
        for read, value in enumerate(nums):
            if value != 0:
                nums[write], nums[read] = nums[read], nums[write]; write += 1
