"""Canonical solution metadata.

Problem Number: 8
Problem Title: String to Integer (atoi)
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: String
Study Tags: Parsing, Overflow Clamping
Canonical URL: https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution:
    def myAtoi(self, text: str) -> int:
        index = 0
        while index < len(text) and text[index] == " ":
            index += 1
        sign = 1
        if index < len(text) and text[index] in "+-":
            sign = -1 if text[index] == "-" else 1
            index += 1
        value = 0
        while index < len(text) and text[index].isdigit():
            value = value * 10 + int(text[index])
            index += 1
        value *= sign
        return max(-(2**31), min(2**31 - 1, value))
