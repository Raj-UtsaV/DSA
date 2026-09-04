# 105 — Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## Topics

Official LeetCode Topics:
- Array
- Hash Table
- Divide and Conquer
- Tree
- Binary Tree

Study Patterns:
- Recursion and Partitioning

## Intuition

The implementation solves construct binary tree from preorder and inorder traversal by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Recursion and Partitioning technique.

## Approach

1. Initialize the state required by the Recursion and Partitioning invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n)
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Recursion and Partitioning pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d050eec34db81adb26cd1ec8d60e2b3?pvs=204
