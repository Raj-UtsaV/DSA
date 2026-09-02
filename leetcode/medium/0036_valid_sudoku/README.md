# 36 — Valid Sudoku

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/valid-sudoku/

## Topics

Official LeetCode Topics:
- Array
- Hash Table
- Matrix

Study Patterns:
- Constraint validation

## Intuition

The implementation solves valid sudoku by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Constraint validation technique.

## Approach

1. Initialize the state required by the Constraint validation invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(1) for the fixed 9 × 9 board
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Constraint validation pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
