# 121 — Best Time to Buy and Sell Stock

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Topics

Official LeetCode Topics:
- Array
- Dynamic Programming

Study Patterns:
- Kadane's Algorithm

## Intuition

The implementation solves best time to buy and sell stock by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Kadane's Algorithm technique.

## Approach

1. Initialize the state required by the Kadane's Algorithm invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Kadane's Algorithm pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db81299f03c833e6b382ba?pvs=204](https://app.notion.com/p/3d050eec34db81299f03c833e6b382ba?pvs=204)
