# 37 — Sudoku Solver

**Difficulty:** Hard

**LeetCode:** https://leetcode.com/problems/sudoku-solver/

## Topics

Official LeetCode Topics:
- Array
- Hash Table
- Backtracking
- Matrix
- Algorithm X
- Dancing Links

Study Patterns:
- Constraint propagation

## Intuition

The valid answers for sudoku solver form a decision tree. The implementation builds one candidate at a time and abandons a branch as soon as it violates a constraint.

## Approach

1. Record the current partial choice and the constraints it already consumes.
2. Try each legal next choice recursively, then undo it before trying the next option.
3. Save or return a candidate when it reaches the required complete state.

## Complexity

- Time: O(9^e), where e is the number of empty cells
- Space: O(e) recursion depth

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Constraint propagation pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
