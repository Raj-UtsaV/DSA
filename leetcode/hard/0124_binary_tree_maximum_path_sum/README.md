# 124 — Binary Tree Maximum Path Sum

**Difficulty:** Hard

**LeetCode:** https://leetcode.com/problems/binary-tree-maximum-path-sum/

## Topics

Official LeetCode Topics:
- Dynamic Programming
- Tree
- Depth-First Search
- Binary Tree
- DP on Trees

Study Patterns:
- Tree DP

## Intuition

The solution to binary tree maximum path sum is composed of repeated smaller states. Storing each state's best result prevents the same subproblem from being solved again.

## Approach

1. Define the state represented by each memo or DP entry.
2. Evaluate valid transitions in an order where required smaller states are available.
3. Return the entry representing the complete input.

## Complexity

- Time: O(n)
- Space: O(h) recursion stack

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Tree DP pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
