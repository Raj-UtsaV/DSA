# 216 — Combination Sum III

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/combination-sum-iii/

## Topics

Official LeetCode Topics:
- Array
- Backtracking

Study Patterns:
- Recursion and Partitioning

## Intuition

The implementation solves combination sum iii by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Recursion and Partitioning technique.

## Approach

1. Initialize the state required by the Recursion and Partitioning invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: Exponential in the number of choices
- Space: O(n) recursion depth, excluding output

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Recursion and Partitioning pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
