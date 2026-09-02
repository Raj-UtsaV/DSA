"""Canonical solution metadata.

Problem Number: 136
Problem Title: Single Number
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Bit Manipulation
Study Tags: XOR Cancellation
Canonical URL: https://leetcode.com/problems/single-number/
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        answer = 0
        for value in nums: answer ^= value
        return answer
