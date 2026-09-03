# 3876 — Construct Uniform Parity Array II

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/construct-uniform-parity-array-ii/

## Topics

Official LeetCode Topics:
- Array
- Math

Study Patterns:
- Greedy
- Parity

## Intuition

An all-even array is already valid. For a mixed-parity array, the only possible target is all odd.

Let `minimum` be the smallest element. It cannot be changed because there is no smaller positive array element that it can subtract. Therefore, a mixed array is possible exactly when `minimum` is odd. Every even element can then subtract this odd minimum, producing a positive odd value, while every odd element can remain unchanged.

## Approach

1. Find the minimum value.
2. If it is odd, return `True`: keep odd values and subtract the minimum from every even value.
3. Otherwise, return whether every value is even.

## Correctness

- If every input is even, keeping every value unchanged constructs an all-even array.
- If the minimum is odd, each odd value can remain unchanged. Each even value is greater than the distinct odd minimum, so subtracting the minimum produces a positive odd value. Thus an all-odd array can be constructed.
- If the minimum is even and the array contains an odd value, the minimum cannot be changed: subtracting any other element would not remain positive. It therefore stays even. The odd value cannot become even by subtracting an even value, and no smaller odd value exists. Hence uniform parity is impossible.

Therefore, the algorithm returns `True` exactly when a uniform-parity array can be constructed.

## Complexity

- Time: O(n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Notion Notes

Detailed explanation, code walkthrough, dry run, and diagrams:

[3876 — Construct Uniform Parity Array II](https://app.notion.com/p/3876-Construct-Uniform-Parity-Array-II-3d050eec34db81ce9c5acdc31a07bb5e)
