"""Canonical solution metadata.

Problem Number: 350
Problem Title: Intersection of Two Arrays II
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Hash Table, Two Pointers, Binary Search, Sorting
Study Tags: Frequency Counting
Canonical URL: https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts, answer = Counter(nums1), []
        for value in nums2:
            if counts[value]: answer.append(value); counts[value] -= 1
        return answer
