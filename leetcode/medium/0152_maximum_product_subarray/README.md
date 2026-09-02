# 152 — Maximum Product Subarray

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/maximum-product-subarray/

## Topics

Official LeetCode Topics:
- Array
- Dynamic Programming

Study Patterns:
- Running minimum and maximum

## Intuition

The implementation solves maximum product subarray by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Running minimum and maximum technique.

## Approach

1. Initialize the state required by the Running minimum and maximum invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Running minimum and maximum pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
