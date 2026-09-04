"""Canonical solution metadata.

Problem Number: 4038
Problem Title: Count Integers Appearing in a Single Block
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Hash Table
Study Tags: Block Counting
Canonical URL: https://leetcode.com/problems/count-integers-appearing-in-a-single-block/
"""


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        frequency = {}

        for index, number in enumerate(nums):
            if number not in frequency:
                frequency[number] = True
            elif nums[index - 1] != number:
                frequency[number] = False

        return sum(frequency.values())
