# 812 — Largest Triangle Area

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/largest-triangle-area/

## Topics

Official LeetCode Topics:
- Array
- Math
- Geometry
- Polygons

Study Patterns:
- Shoelace formula

## Intuition

The implementation solves largest triangle area by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Shoelace formula technique.

## Approach

1. Initialize the state required by the Shoelace formula invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n³)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Shoelace formula pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db819a836ae463419d3c5b?pvs=204](https://app.notion.com/p/3d050eec34db819a836ae463419d3c5b?pvs=204)
