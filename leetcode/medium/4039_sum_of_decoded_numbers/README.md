# 4039 — Sum of Decoded Numbers

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/sum-of-decoded-numbers/

## Topics

Official LeetCode Topics:
- Array
- Math

Study Patterns:
- Modular Exponentiation
- Digit Decoding

## Intuition

The final digit stores the width of `x`. Removing that digit leaves the decimal digits of `x` followed by `y`. Split those digits at the stored width, then calculate `x^y` with modular exponentiation.

## Approach

1. Read the final digit as `width`.
2. Remove it using integer division by 10.
3. Split the remaining decimal representation after `width` digits.
4. Decode the left part as the base and the right part as the exponent.
5. Add `pow(base, exponent, 1_000_000_007)` to the answer modulo the same value.

## Complexity

- Time: O(n log Y), where `Y` is the largest decoded exponent
- Space: O(D), where `D` is the maximum number of encoded digits

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Use `number // 10`; floating-point `floor(number / 10)` can lose precision for large integers.
- Python's three-argument `pow` performs efficient modular exponentiation.
- Apply the modulus while accumulating, not only after potentially huge powers are constructed.

## Notion Notes

Detailed explanation, code walkthrough and dry run:

Notion page: https://app.notion.com/p/3d150eec34db81c590a6eeaaa9657e0d?pvs=204
