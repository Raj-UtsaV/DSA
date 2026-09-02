# 930 — Binary Subarrays With Sum

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/binary-subarrays-with-sum/

## Topics

Official LeetCode Topics:
- Array
- Hash Table
- Sliding Window
- Prefix Sum

Study Patterns:
- Prefix Sum and Prefix Frequency

## Intuition

The implementation solves binary subarrays with sum by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Prefix Sum and Prefix Frequency technique.

## Approach

1. Initialize the state required by the Prefix Sum and Prefix Frequency invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n)
- Space: O(k), for the maintained frequency state

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Prefix Sum and Prefix Frequency pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
