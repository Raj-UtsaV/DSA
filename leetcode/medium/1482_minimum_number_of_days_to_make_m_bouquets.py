"""Canonical solution metadata.

Problem Number: 1482
Problem Title: Minimum Number of Days to Make m Bouquets
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Binary Search
Study Tags: Binary Search on Answer
Canonical URL: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
"""

class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        def possible(day):
            bouquets = run = 0
            for bloom in bloomDay:
                run = run + 1 if bloom <= day else 0
                if run == k: bouquets += 1; run = 0
            return bouquets >= m
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if possible(mid): right = mid
            else: left = mid + 1
        return left
