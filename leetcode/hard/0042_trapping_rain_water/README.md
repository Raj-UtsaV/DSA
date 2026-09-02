# 42 — Trapping Rain Water

**Difficulty:** Hard

**LeetCode:** https://leetcode.com/problems/trapping-rain-water/

## Topics

Official LeetCode Topics:
- Array
- Two Pointers
- Dynamic Programming
- Stack
- Monotonic Stack

Study Patterns:
- Two Pointers

## Intuition

Water above a bar is limited by the smaller maximum boundary on its two sides. When the left maximum is no greater than the right maximum, the left position can be resolved immediately; otherwise, the right position can be resolved.

## Approach

1. Place pointers at both ends and track the maximum height reached from each side.
2. Process the side with the smaller current maximum.
3. Add the difference between that maximum and the current height, then move its pointer inward.

## Complexity

- Time: O(n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- The smaller boundary determines the water level that is currently safe to finalize.
- Flat, increasing, decreasing, and empty inputs trap no water.
- Update the side maximum before adding water to avoid negative contributions.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
