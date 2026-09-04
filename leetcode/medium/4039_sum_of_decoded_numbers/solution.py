"""Canonical solution metadata.

Problem Number: 4039
Problem Title: Sum of Decoded Numbers
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Math
Study Tags: Modular Exponentiation, Digit Decoding
Canonical URL: https://leetcode.com/problems/sum-of-decoded-numbers/
"""


class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        modulo = 1_000_000_007
        total = 0

        for number in nums:
            width = number % 10
            digits = str(number // 10)

            base = int(digits[:width])
            exponent = int(digits[width:])

            total = (total + pow(base, exponent, modulo)) % modulo

        return total
