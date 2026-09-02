# Ceil in a Binary Search Tree

**Difficulty:** Not reliably specified

**Platform:** GeeksforGeeks

**Problem:** https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1

## Topics

Study Topics:
- Binary Search Tree

Study Patterns:
- Tree DFS and BFS

## Intuition

The candidate values for ceil in a binary search tree have an ordered or monotonic structure. Binary search can discard half of the remaining range after each comparison or feasibility check.

## Approach

1. Choose bounds that contain every possible answer.
2. Evaluate the midpoint using the implementation's comparison or feasibility condition.
3. Move the invalid boundary until the search converges, then return the surviving candidate.

## Complexity

- Time: O(n)
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Tree DFS and BFS pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
