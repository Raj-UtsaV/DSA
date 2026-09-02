# 41 — First Missing Positive

**Difficulty:** Hard

**LeetCode:** https://leetcode.com/problems/first-missing-positive/

## Topics

Official LeetCode Topics:
- Array
- Hash Table

Study Patterns:
- Cyclic placement

## Intuition

The implementation solves first missing positive by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Cyclic placement technique.

## Approach

1. Initialize the state required by the Cyclic placement invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n log n)
- Space: O(n) for Python's sorting machinery

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Cyclic placement pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
