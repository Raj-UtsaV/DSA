"""LeetCode 3876 — Construct Uniform Parity Array II.

Difficulty: Medium
Topics: Array, Math
Approaches: Brute Force, Sorting, Optimal Greedy
Problem: https://leetcode.com/problems/construct-uniform-parity-array-ii/
Notes: https://app.notion.com/p/3876-Construct-Uniform-Parity-Array-II-3d050eec34db81ce9c5acdc31a07bb5e
"""


class SolutionBrute:
    """Brute force: try to make the whole array even or the whole array odd."""

    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)

        even_ans = True
        for i in range(n):
            if nums1[i] % 2 != 0:
                found = False
                for num in nums1:
                    value = nums1[i] - num
                    if value >= 1 and value % 2 == 0:
                        found = True
                        break
                if not found:
                    even_ans = False
                    break

        odd_ans = True
        for i in range(n):
            if nums1[i] % 2 == 0:
                found = False
                for num in nums1:
                    value = nums1[i] - num
                    if value >= 1 and value % 2 != 0:
                        found = True
                        break
                if not found:
                    odd_ans = False
                    break

        return odd_ans or even_ans


class SolutionSort:
    """Better: sort so the minimum element is available immediately."""

    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        return nums1[0] % 2 != 0 or all(x % 2 == 0 for x in nums1)


class Solution:
    """Optimal: only the parity of the minimum and whether all values are even matter."""

    def uniformArray(self, nums1: list[int]) -> bool:
        return (min(nums1) % 2 != 0) or all(x % 2 == 0 for x in nums1)
