# 54 — Spiral Matrix

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/spiral-matrix/

## Topics

Official LeetCode Topics:
- Array
- Matrix
- Simulation

Study Patterns:
- Matrix and Grid Traversal
- Tree DFS and BFS

## Intuition

The result for spiral matrix follows from information collected while traversing the tree. Each node is processed once, with recursion or a queue preserving the required traversal order.

## Approach

1. Handle the empty-node base case.
2. Traverse the required child nodes and update or combine their information at the current node.
3. Return the value accumulated for the root or traversal output.

## Complexity

- Time: O(n)
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Matrix and Grid Traversal pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db816bb6fedb6770142b47?pvs=204](https://app.notion.com/p/3d050eec34db816bb6fedb6770142b47?pvs=204)
