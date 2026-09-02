# 987 — Vertical Order Traversal of a Binary Tree

**Difficulty:** Hard

**LeetCode:** https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

## Topics

Official LeetCode Topics:
- Hash Table
- Tree
- Depth-First Search
- Breadth-First Search
- Sorting
- Binary Tree

Study Patterns:
- Sorting and Partitioning

## Intuition

The implementation solves vertical order traversal of a binary tree by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Sorting and Partitioning technique.

## Approach

1. Initialize the state required by the Sorting and Partitioning invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n log n)
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Sorting and Partitioning pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
