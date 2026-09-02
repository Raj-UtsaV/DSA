"""Canonical solution metadata.

Problem Number: 169
Problem Title: Majority Element
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm
Study Tags: Boyer-Moore Voting
Canonical URL: https://leetcode.com/problems/majority-element/
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = count = 0
        for value in nums:
            if count == 0: candidate = value
            count += 1 if value == candidate else -1
        return candidate
