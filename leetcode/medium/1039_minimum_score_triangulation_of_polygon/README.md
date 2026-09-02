# 1039 — Minimum Score Triangulation of Polygon

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

## Topics

Official LeetCode Topics:
- Array
- Dynamic Programming
- Triangulation
- Polygons

Study Patterns:
- Interval DP

## Intuition

The solution to minimum score triangulation of polygon is composed of repeated smaller states. Storing each state's best result prevents the same subproblem from being solved again.

## Approach

1. Define the state represented by each memo or DP entry.
2. Evaluate valid transitions in an order where required smaller states are available.
3. Return the entry representing the complete input.

## Complexity

- Time: O(n³)
- Space: O(n²)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Interval DP pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
