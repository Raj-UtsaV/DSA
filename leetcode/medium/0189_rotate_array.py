"""Canonical solution metadata.

Problem Number: 189
Problem Title: Rotate Array
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Math, Two Pointers
Study Tags: Reversal Algorithm
Canonical URL: https://leetcode.com/problems/rotate-array/
"""

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if not nums: return
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k] if k else nums
