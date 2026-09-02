"""Canonical solution metadata.

Problem Number: 78
Problem Title: Subsets
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Backtracking, Bit Manipulation
Study Tags: Include-Exclude Recursion
Canonical URL: https://leetcode.com/problems/subsets/
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        answer: list[list[int]] = []

        def visit(index: int, current: list[int]) -> None:
            if index == len(nums):
                answer.append(current.copy())
                return
            visit(index + 1, current)
            current.append(nums[index])
            visit(index + 1, current)
            current.pop()

        visit(0, [])
        return answer
