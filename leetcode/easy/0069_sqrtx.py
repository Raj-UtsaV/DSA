"""Canonical solution metadata.

Problem Number: 69
Problem Title: Sqrt(x)
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Math, Binary Search, Newton's Method
Study Tags: Answer-Space Search
Canonical URL: https://leetcode.com/problems/sqrtx/
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x: left = mid + 1
            else: right = mid - 1
        return right
