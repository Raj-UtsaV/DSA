# 173 — Binary Search Tree Iterator

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/binary-search-tree-iterator/

## Topics

Official LeetCode Topics:
- Stack
- Tree
- Design
- Binary Search Tree
- Binary Tree
- Iterator

Study Patterns:
- Tree DFS and BFS

## Intuition

An inorder traversal yields BST values in sorted order, but it need not be materialized eagerly. A stack stores only the path to the next smallest node.

## Approach

1. Push the root and its entire left chain.
2. For next, pop the smallest pending node and push the left chain of its right subtree.
3. Report whether another value exists by checking the stack.

## Complexity

- Time: O(1) amortized per next call
- Space: O(h)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Tree DFS and BFS pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
