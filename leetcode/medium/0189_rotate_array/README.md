# 189 — Rotate Array

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/rotate-array/

## Topics

Official LeetCode Topics:
- Array
- Math
- Two Pointers

Study Patterns:
- Reversal Algorithm

## Intuition

The implementation solves rotate array by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Reversal Algorithm technique.

## Approach

1. Initialize the state required by the Reversal Algorithm invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Reversal Algorithm pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
