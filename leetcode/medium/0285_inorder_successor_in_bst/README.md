# 285 — Inorder Successor in BST

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/inorder-successor-in-bst/

## Topics

Official LeetCode Topics:
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree

Study Patterns:
- Greedy

## Intuition

A locally optimal choice for inorder successor in bst leaves the greatest flexibility for the remaining input. Ordering the candidates makes that safe choice available at each step.

## Approach

1. Order candidates by the criterion used by the greedy invariant.
2. Accept a candidate when it is compatible with the choices already made.
3. Return the accumulated count, value, or selected arrangement.

## Complexity

- Time: O(n)
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Greedy pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
