"""Canonical solution metadata.

Problem Number: 1539
Problem Title: Kth Missing Positive Number
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Binary Search
Study Tags: Missing-Count Invariant
Canonical URL: https://leetcode.com/problems/kth-missing-positive-number/
"""

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 < k: left = mid + 1
            else: right = mid
        return left + k
