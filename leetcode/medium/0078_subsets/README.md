# 78 — Subsets

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/subsets/

## Topics

Official LeetCode Topics:
- Array
- Backtracking
- Bit Manipulation

Study Patterns:
- Recursion and Partitioning

## Intuition

The valid answers for subsets form a decision tree. The implementation builds one candidate at a time and abandons a branch as soon as it violates a constraint.

## Approach

1. Record the current partial choice and the constraints it already consumes.
2. Try each legal next choice recursively, then undo it before trying the next option.
3. Save or return a candidate when it reaches the required complete state.

## Complexity

- Time: O(n · 2^n)
- Space: O(n) auxiliary space, excluding output

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Recursion and Partitioning pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d050eec34db811a928ff28b2e95d9da?pvs=204
