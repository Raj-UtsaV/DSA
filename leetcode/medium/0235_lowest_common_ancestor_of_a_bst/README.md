# 235 — Lowest Common Ancestor of a Binary Search Tree

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

## Topics

Official LeetCode Topics:
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree
- Binary Lifting
- Lowest Common Ancestor

Study Patterns:
- Lowest Common Ancestor
- Tree DFS and BFS

## Intuition

The result for lowest common ancestor of a binary search tree follows from information collected while traversing the tree. Each node is processed once, with recursion or a queue preserving the required traversal order.

## Approach

1. Handle the empty-node base case.
2. Traverse the required child nodes and update or combine their information at the current node.
3. Return the value accumulated for the root or traversal output.

## Complexity

- Time: O(n)
- Space: O(h) recursion stack

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Lowest Common Ancestor pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db8118b0b8d47f79951a22?pvs=204
