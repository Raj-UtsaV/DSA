"""Canonical solution metadata.

Problem Number: 560
Problem Title: Subarray Sum Equals K
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Hash Table, Prefix Sum
Study Tags: Prefix-Frequency Map
Canonical URL: https://leetcode.com/problems/subarray-sum-equals-k/
"""

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        seen, total, answer = defaultdict(int, {0: 1}), 0, 0
        for value in nums: total += value; answer += seen[total-k]; seen[total] += 1
        return answer
