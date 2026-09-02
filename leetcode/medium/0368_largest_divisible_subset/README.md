# 368 — Largest Divisible Subset

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/largest-divisible-subset/

## Topics

Official LeetCode Topics:
- Array
- Math
- Dynamic Programming
- Sorting

Study Patterns:
- Longest Increasing Subsequence
- Subsequence DP

## Intuition

The solution to largest divisible subset is composed of repeated smaller states. Storing each state's best result prevents the same subproblem from being solved again.

## Approach

1. Define the state represented by each memo or DP entry.
2. Evaluate valid transitions in an order where required smaller states are available.
3. Return the entry representing the complete input.

## Complexity

- Time: O(n²)
- Space: O(n), excluding output

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Longest Increasing Subsequence pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
