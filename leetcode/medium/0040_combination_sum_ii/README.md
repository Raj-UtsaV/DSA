# 40 — Combination Sum II

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/combination-sum-ii/

## Topics

Official LeetCode Topics:
- Array
- Backtracking

Study Patterns:
- Backtracking

## Intuition

The valid answers for combination sum ii form a decision tree. The implementation builds one candidate at a time and abandons a branch as soon as it violates a constraint.

## Approach

1. Record the current partial choice and the constraints it already consumes.
2. Try each legal next choice recursively, then undo it before trying the next option.
3. Save or return a candidate when it reaches the required complete state.

## Complexity

- Time: O(2^n · n) in the worst case
- Space: O(n) auxiliary space, excluding output

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Backtracking pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db81c8a454dd2b3ec14916?pvs=204](https://app.notion.com/p/3d050eec34db81c8a454dd2b3ec14916?pvs=204)
