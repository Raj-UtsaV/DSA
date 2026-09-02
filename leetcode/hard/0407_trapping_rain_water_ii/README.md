# 407 — Trapping Rain Water II

**Difficulty:** Hard

**LeetCode:** https://leetcode.com/problems/trapping-rain-water-ii/

## Topics

Official LeetCode Topics:
- Array
- Breadth-First Search
- Heap (Priority Queue)
- Matrix

Study Patterns:
- Boundary expansion

## Intuition

The implementation solves trapping rain water ii by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Boundary expansion technique.

## Approach

1. Initialize the state required by the Boundary expansion invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(mn log(mn))
- Space: O(mn)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Boundary expansion pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
