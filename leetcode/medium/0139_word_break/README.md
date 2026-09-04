# 139 — Word Break

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/word-break/

## Topics

Official LeetCode Topics:
- Array
- Hash Table
- String
- Dynamic Programming
- Trie
- Memoization
- Brute-Force Search

Study Patterns:
- Dynamic Programming

## Intuition

The solution to word break is composed of repeated smaller states. Storing each state's best result prevents the same subproblem from being solved again.

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

Notion page: https://app.notion.com/p/3d050eec34db812592c8d893f3cda4c7?pvs=204
