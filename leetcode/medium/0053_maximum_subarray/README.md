# 53 — Maximum Subarray

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/maximum-subarray/

## Topics

Official LeetCode Topics:
- Array
- Divide and Conquer
- Dynamic Programming

Study Patterns:
- Kadane's Algorithm

## Intuition

At each position, the best subarray ending there either starts with the current value or extends the previous best ending there. Tracking the greatest such ending value seen so far yields the global optimum.

## Approach

1. Initialize both the current sum and best sum with the first element.
2. For each remaining value, choose between starting fresh and extending the current subarray.
3. Update the best sum after each choice.

## Complexity

- Time: O(n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- This is the classic Kadane's Algorithm recurrence.
- Initializing from the first element correctly handles arrays containing only negative values.
- Reset based on the current value, not an assumed zero baseline.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
