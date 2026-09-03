"""Canonical solution metadata.

Problem Number: 893
Problem Title: Groups of Special-Equivalent Strings
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Hash Table, String, Sorting
Canonical URL: https://leetcode.com/problems/groups-of-special-equivalent-strings/
"""

from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()

        for word in words:
            signature = tuple(sorted(word[::2]) + sorted(word[1::2]))
            groups.add(signature)

        return len(groups)
