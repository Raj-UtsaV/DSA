# 104 — Maximum Depth of Binary Tree

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Topics

Official LeetCode Topics:
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree

Study Patterns:
- Tree DFS and BFS
- Tree DP

## Intuition

The solution to maximum depth of binary tree is composed of repeated smaller states. Storing each state's best result prevents the same subproblem from being solved again.

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

- Recognize this problem when its constraints match the Tree DFS and BFS pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db81978374dc95710738f0?pvs=204](https://app.notion.com/p/3d050eec34db81978374dc95710738f0?pvs=204)
