# 673 — Number of Longest Increasing Subsequence

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/number-of-longest-increasing-subsequence/

## Topics

Official LeetCode Topics:
- Array
- Dynamic Programming
- Binary Indexed Tree
- Segment Tree
- Longest Increasing Subsequence

Study Patterns:
- Dynamic Programming
- Subsequence DP

## Intuition

The solution to number of longest increasing subsequence is composed of repeated smaller states. Storing each state's best result prevents the same subproblem from being solved again.

## Approach

1. Define the state represented by each memo or DP entry.
2. Evaluate valid transitions in an order where required smaller states are available.
3. Return the entry representing the complete input.

## Complexity

- Time: O(n²)
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Dynamic Programming pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db814d83e3c18a59388b84?pvs=204
