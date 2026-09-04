# 98 — Validate Binary Search Tree

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/validate-binary-search-tree/

## Topics

Official LeetCode Topics:
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree

Study Patterns:
- Range Validation

## Intuition

The implementation solves validate binary search tree by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Range Validation technique.

## Approach

1. Initialize the state required by the Range Validation invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n)
- Space: O(h) recursion stack

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Range Validation pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d050eec34db8172bb4fe03d2923763c?pvs=204
